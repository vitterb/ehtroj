import platform
import os

def run(**args):
    if platform == "win32":
        return ("machine type:" + platform.machine() + "/n"+
                "machine network name: "+ platform.nod() + "/n" +
                "processor name: " + platform.processor() + "/n" +
                "Windows Edition: " + platform.win32_edition())
    else:
        return ("machine type: " + platform.machine() + "/n"+
                "machine network name: "+ platform.nod() + "/n" +
                "processor name: " + platform.processor() + "/n" +
                "Linux os: " + platform.freedesktop_os_release())