import platform
from sys import platform as plat

def run(**args):

    if plat == "win32":
        f = open("./data/windows.txt", "a")
        f.write("machine type:" + platform.machine() + "\n"+
                "machine network name: "+ platform.node() + "\n" +
                "processor name: " + platform.processor() + "\n" +
                "Windows info: " + ' '.join(platform.win32_ver()) + "\n" +
                "Windows Edition: " + platform.win32_edition())
        f.close()
        return ("machine type:" + platform.machine() + "\n"+
                "machine network name: "+ platform.node() + "\n" +
                "processor name: " + platform.processor() + "\n" +
                "Windows info: " + ' '.join(platform.win32_ver()) + "\n" +
                "Windows Edition: " + platform.win32_edition())
    else:
        f = open("./data/linux.txt", "a")
        f.write("machine type: " + platform.machine() + "\n"+
                "machine network name: "+ platform.node() + "\n" +
                "processor name: " + platform.processor() + "\n" +
                "Linux os: " + platform.freedesktop_os_release())
        f.close()
        return  ("machine type: " + platform.machine() + "\n"+
                "machine network name: "+ platform.node() + "\n" +
                "processor name: " + platform.processor() + "\n" +
                "Linux os: " + platform.freedesktop_os_release())