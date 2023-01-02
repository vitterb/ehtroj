import platform

def run(**args):
    return  ("machine type:" + platform.machine() + "\n"+
            "machine network name: "+ platform.node() + "\n" +
            "processor name: " + platform.processor() + "\n" +
            "Windows info: " + ' '.join(platform.win32_ver()) + "\n" +
            "Windows Edition: " + platform.win32_edition())