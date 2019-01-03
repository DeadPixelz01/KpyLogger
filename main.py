# stores a user's keystrokes in a local text file

# file_a = file append
# file_r = file read


# creates and writes to a local text file called 'usr_log'
def append_to_log():
    file_a = open('usr_log.txt', 'a')
    # writes string to file
    file_a.write('Testing!\n')
    # close the file
    file_a.close()


def read_from_log():
    # reads from a local text file called 'usr_log'
    file_r = open('usr_log.txt', 'r')
    # creates a variable for the contents of the text file
    file_data = file_r.read()
    # prints the contents of the text file
    print(file_data)
    # close the file
    file_r.close()
