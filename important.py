#this file controls web browsers, any change to this file may break whole program
import keyboard
import time

def zoomJoin():
    time.sleep(5)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)

