from cx_Freeze import Executable, setup
import sys
sys.setrecursionlimit(10000)

build_exe_options = {
    "include_files" : ["bullet.png","ufo.png", "rocket.png", "galaxy.jpg"]
}

base = None 
if sys.platform == "win32":
    base = "win32GUI"


setup(
    name = "Shooter Game",
    version = "1.0",
    decription = "...",
    options = {"build_exe" : build_exe_options},
    executables = [Executable("current.py", base = base)]
)