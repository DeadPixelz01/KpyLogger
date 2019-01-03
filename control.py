# imports
from main import mouse_append_to_log
from main import key_append_to_log
from pynput.mouse import Controller
from pynput.keyboard import Controller
from pynput.keyboard import Listener
from pynput.mouse import Listener


# controls the position of the user's mouse
def mouse_control(position):
    # create a variable called mouse and set it to use the controller function
    mouse = Controller()
    # move the mouse to a position (x,y) (always starts from top-left of screen)
    mouse.position = position


# types out a string using the user's keyboard
def keyboard_control(typed_phrase):
    # create a variable called keyboard and set it to use the controller function
    keyboard = Controller()
    # type out the string
    keyboard.type(typed_phrase)


# listens for keystrokes and mouse movement
def keyboard_mouse_listen():
    with Listener(on_move=mouse_append_to_log) as mouse_l, Listener(on_press=key_append_to_log) as key_l:
        mouse_l.join(), key_l.join()


keyboard_mouse_listen()
