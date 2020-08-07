
__version__ = '0.1.0'

# YOWASP:

def populate_environ():
    import os, shutil

    for nmigen_envvar, expected_path, alternative_path in [
            ("YOSYS",         "yosys",         "yowasp-yosys"), # nmigen-yosys is handled by nmigen
            ("NEXTPNR_ICE40", "nextpnr-ice40", "yowasp-nextpnr-ice40"),
            ("NEXTPNR_ECP5",  "nextpnr-ecp5",  "yowasp-nextpnr-ecp5"),
        ]:
        if nmigen_envvar in os.environ: continue
        if shutil.which(expected_path): continue
        if not shutil.which(alternative_path): continue
        os.environ[nmigen_envvar] = alternative_path

populate_environ()
del populate_environ

# dogelang: Slow. Stupid. Absolutely adorable.
import dg # setup the dg import hook
