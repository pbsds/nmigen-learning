
__version__ = '0.1.0'

# YOWASP:

def populate_environ():
    import os, shutil

    for env_name, program in [
            ("YOSYS",         "yowasp-yosys"),
            ("NEXTPNR_ICE40", "yowasp-nextpnr-ice40"),
            ("NEXTPNR_ECP5",  "yowasp-nextpnr-ecp5"),
        ]:
        if shutil.which(program):
            os.environ[env_name] = program

populate_environ()
del populate_environ

# dogelang: Slow. Stupid. Absolutely adorable.
import dg # install import hook
