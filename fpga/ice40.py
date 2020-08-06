from nmigen import *
from nmigen.cli import main
from nmigen_boards.icebreaker import ICEBreakerPlatform

class Blinker(Elaboratable):
    def __init__(self, maxperiod: int):
        self.maxperiod = maxperiod

    def elaborate(self, platform):
        led = platform.request("led_r")

        m = Module()

        counter = Signal(range(self.maxperiod + 1))

        with m.If(counter == 0):
            m.d.sync += [
                led.eq(~led),
                counter.eq(self.maxperiod)
            ]
        with m.Else():
            m.d.sync += counter.eq(counter - 1)

        return m


if __name__ == "__main__":
    plat = ICEBreakerPlatform()
    #main(plat, ports=[plat.led])
    plat.build(Blinker(10000000), do_program=True)

