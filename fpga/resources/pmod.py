from nmigen.build import *
from functools import partial

__all__ = []
def pmod(func):
    __all__.append(func.__name__)
    return partial(func,
        name = func.__name__,
    )


# Icebreaker PMODs

#subsignal_args = [Attrs(IO_STANDARD="SB_LVCMOS33")]

@pmod
def seven_seg(number, *, pmod, name = __name__, subsignal_args=(), extras={}):
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
def dip_switch8(number, *, pmod, name = __name__, subsignal_args=(), extras={}):
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
