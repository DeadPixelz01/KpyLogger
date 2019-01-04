# imports
from main import append_to_log
from pynput.keyboard import Controller
from pynput.keyboard import Listener


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


def keyboard_listen():
    with Listener(on_press=append_to_log) as key_l:
        key_l.join()


keyboard_listen()