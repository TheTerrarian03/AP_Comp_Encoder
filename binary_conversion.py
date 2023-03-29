import library

def get_user_message():

def binary_conversion(message):
    ascii_values = [] # List for ascii values
    binary_values = [] # List for final binary message

    for letter in message: # Iterates through string and applies ascii value
        ascii_values.append(ord(letter))

    for value in ascii_values: # Turns ascii to binary
        binary_values.append(bin(value)[2:])

    return binary_values 

# Syncs binary to sound
def sync_message(binary_values):
    for binary_values in library.notes_and_letters


print(binary_conversion('hello'))