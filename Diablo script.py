import pydirectinput
import keyboard
import time


def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'f4':
            pydirectinput.press ('escape')
            pydirectinput.press ('down')
            pydirectinput.press ('enter')
            pydirectinput.press ('up')
            pydirectinput.press ('up')
            pydirectinput.press ('enter')
            pydirectinput.press ('escape')
            print ("I did the thing")
            
            
            
print ("hello, it is working")
keyboard.hook(on_key_event)
keyboard.wait('=')
