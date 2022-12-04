import pyscreenshot as ImageGrab

def run(**args):
    # grab fullscreen
    im = ImageGrab.grab()
    # save image file
    im.save("fullscreen.png")

    with open("fullscreen.png", "rb") as image:
        img = image.read()
        return img
