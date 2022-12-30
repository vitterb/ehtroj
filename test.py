from sys import platform

if platform == "win32":
    print("windows")
else:
    var = platform.uname()
    print("var")