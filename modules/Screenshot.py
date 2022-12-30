from mss import mss

def run(**args):
   # The simplest use, save a screen shot of the 1st monitor
    with mss() as sct:
        img = sct.shot()

    return img