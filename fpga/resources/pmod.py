from nmigen.build import *

__ALL__ = [
    "seven_seg",
]

# Icebreaker PMODs

def seven_seg(pmod_port: int, name="seven_seg"):
    conn = ("pmod", pmod_port)
    return [
        Resource(name, 0,
             Subsignal("aa", PinsN( "1", dir="o", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("ab", PinsN( "2", dir="o", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("ac", PinsN( "3", dir="o", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("ad", PinsN( "4", dir="o", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("ae", PinsN( "7", dir="o", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("af", PinsN( "8", dir="o", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("ag", PinsN( "9", dir="o", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("ca", PinsN("10", dir="o", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
         )
    ]

def dip_switch8(pmod_port: int, name="dip_switch8"):
    return [
        Resource(name, 0,
             Subsignal("d1", PinsN( "1", dir="i", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("d2", PinsN( "2", dir="i", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("d3", PinsN( "3", dir="i", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("d4", PinsN( "4", dir="i", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("d5", PinsN( "7", dir="i", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("d5", PinsN( "8", dir="i", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("d6", PinsN( "9", dir="i", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
             Subsignal("d8", PinsN("10", dir="i", conn=conn), Attrs(IO_STANDARD="SB_LVCMOS33")),
         )
    ]
