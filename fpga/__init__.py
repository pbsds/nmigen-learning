__version__ = '0.1.0'

def load_env():
    import os, shutil


    if shutil.which("yowasp-yosys"):
        os.environ["NEXTPNR_ICE40"] = "yowasp-nextpnr-ice40"

    if shutil.which("yowasp-nextpnr-ice40"):
        os.environ["NEXTPNR_ICE40"] = "yowasp-nextpnr-ice40"

    if shutil.which("yowasp-nextpnr-ecp5"):
        os.environ["NEXTPNR_ECP5"]  = "yowasp-nextpnr-ecp5"

load_env()
del load_env
