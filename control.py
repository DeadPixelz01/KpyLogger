# imports
from pynput.keyboard import Controller


# types out a string using the user's keyboard
def keyboard_control(typed_phrase):
    # create a variable called keyboard and set it to use the controller function
    keyboard = Controller()
    # type out the string
    keyboard.type(typed_phrase)
