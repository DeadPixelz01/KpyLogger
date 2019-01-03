# imports
from pynput.mouse import Controller
from pynput.keyboard import Controller


# controls the position of the user's mouse
def mouse_control(position):
    # create a variable called mouse and set it to use the controller function
    mouse = Controller()
    # move the mouse to a position (x,y) (always starts from top-left of screen)
    mouse.position = position


def keyboard_control(typed_phrase):
    keyboard = Controller()
    keyboard.type(typed_phrase)


# Testing this on user input
usr_mouse = input('Enter a mouse position: ')
usr_typed_phrase = input('Enter a phrase you wish to type: ')
mouse_control(usr_mouse)
keyboard_control(usr_typed_phrase)
