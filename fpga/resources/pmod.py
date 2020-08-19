from nmigen.build import *
from functools import partial

__all__ = []
def pmod(func):
    __all__.append(func.__name__)
    return partial(func, name=func.__name__)


# Icebreaker PMODs

#subsignal_args = [Attrs(IO_STANDARD="SB_LVCMOS33")]

@pmod
def seven_seg(number, *, pmod, name=__name__, subsignal_args=(), extras={}):
    return [Resource(name, number,
         Subsignal("aa", PinsN( "1", dir="o", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("ab", PinsN( "2", dir="o", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("ac", PinsN( "3", dir="o", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("ad", PinsN( "4", dir="o", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("ae", PinsN( "7", dir="o", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("af", PinsN( "8", dir="o", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("ag", PinsN( "9", dir="o", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("ca", PinsN("10", dir="o", conn=("pmod", pmod)), *subsignal_args),
         **extras,
     )]


@pmod
def dip_switch8(number, *, pmod, name=__name__, subsignal_args=(), extras={}):
    return [Resource(name, number,
         Subsignal("d1", PinsN( "1", dir="i", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("d2", PinsN( "2", dir="i", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("d3", PinsN( "3", dir="i", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("d4", PinsN( "4", dir="i", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("d5", PinsN( "7", dir="i", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("d5", PinsN( "8", dir="i", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("d6", PinsN( "9", dir="i", conn=("pmod", pmod)), *subsignal_args),
         Subsignal("d8", PinsN("10", dir="i", conn=("pmod", pmod)), *subsignal_args),
         **extras,
     )]


@pmod
def dvi_3bit(number, *, pmod, name=__name__, subsignal_args=(), extras={}):
    #                    3b PMOD Connector - Facing module pins
    #                        ----------------------------
    #                       | 1-G 3-CK 5-HS  7-NC GND 3V |
    #                       | 0-R 2-B  4-DE  6-VS GND 3V |
    #                    ___|____________________________|___
    #                   |    BML HDMI 3b color PMOD board    |
    #                    ------------------------------------
    return [Resource(name, number,
        Subsignal("r",  Pins (" 7", dir="o", conn=("pmod", pmod)), *subsignal_args), # red
        Subsignal("g",  Pins (" 1", dir="o", conn=("pmod", pmod)), *subsignal_args), # green
        Subsignal("b",  Pins (" 8", dir="o", conn=("pmod", pmod)), *subsignal_args), # blue
        Subsignal("ck", Pins (" 2", dir="o", conn=("pmod", pmod)), *subsignal_args), # data clock
        Subsignal("de", Pins (" 9", dir="o", conn=("pmod", pmod)), *subsignal_args), # data enable
        Subsignal("hs", Pins (" 3", dir="o", conn=("pmod", pmod)), *subsignal_args), # hsync
        Subsignal("vs", Pins ("10", dir="o", conn=("pmod", pmod)), *subsignal_args), # vsync
        #Subsignal("", Pins (" 4", dir="o", conn=("pmod", pmod)), *subsignal_args),
        **extras,
    )]


@pmod
def dvi_12bit(number, *, pmod1=0, pmod2=1, name=__name__, subsignal_args=(), extras={}):
    #                         12b Module - Facing PMOD pins
    #                 J0                                    J1
    #      ----------------------------        ----------------------------
    #     | 1-R3 3-R1 5-G3 7-G1 GND 3V |      | 1-B3 3-ck 5-B0 7-HS GND 3V |
    #     | 0-R2 2-R0 4-G2 6-G0 GND 3V |      | 0-B2 2-B1 4-DE 6-VS GND 3V |
    #  ___|____________________________|______|____________________________|__
    # |       BML HDMI 12b color PMOD board                                   |
    #  -----------------------------------------------------------------------
    return [Resource(name, number,
        Subsignal("r",  Pins (" 8 2 7 1", dir="o", conn=("pmod", pmod1)), *subsignal_args), # red
        Subsignal("g",  Pins ("10 4 9 3", dir="o", conn=("pmod", pmod1)), *subsignal_args), # green
        Subsignal("b",  Pins (" 3 8 7 1", dir="o", conn=("pmod", pmod2)), *subsignal_args), # blue
        Subsignal("ck", Pins (" 2", dir="o", conn=("pmod", pmod2)), *subsignal_args),       # data clock
        Subsignal("de", Pins (" 9", dir="o", conn=("pmod", pmod2)), *subsignal_args),       # data enable
        Subsignal("hs", PinsN(" 4", dir="o", conn=("pmod", pmod2)), *subsignal_args),       # hsync
        Subsignal("vs", Pins ("10", dir="o", conn=("pmod", pmod2)), *subsignal_args),       # vsync
        **extras,
    )]
