# stores a user's keystrokes in a local text file

# file_a = file append
# file_r = file read

file_name = 'usr_log.txt'


# creates and writes to a local text file called 'usr_log'
def append_to_log(keystrokes):
    keystroke_data = str(keystrokes)
    with open(file_name, 'a') as file_a:
        # writes string to file
        file_a.write(keystroke_data)


def read_from_log(file):
    # reads from a local text file called 'usr_log'
    with open(file, 'r') as file_r:
        # creates a variable for the contents of the text file
        file_data = file_r.read()
        # prints the contents of the text file
        print(file_data)
