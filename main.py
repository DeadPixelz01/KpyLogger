# stores a user's keystrokes in a local text file

# file_a = file append
# file_r = file read


# creates and writes to a local text file called 'usr_log'
def append_to_log(file, keystrokes):
    with open(file, 'a') as file_a:
        # writes string to file
        file_a.write(keystrokes + '\n')


def read_from_log(file):
    # reads from a local text file called 'usr_log'
    with open(file, 'r') as file_r:
        # creates a variable for the contents of the text file
        file_data = file_r.read()
        # prints the contents of the text file
        print(file_data)


# Testing this on user input
usr_file = input('Enter a filename: ')
usr_input = input('Please enter a string: ')
append_to_log(usr_file, usr_input)
read_from_log(usr_file)
