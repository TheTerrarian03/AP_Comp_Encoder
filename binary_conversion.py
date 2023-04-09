import library, tkinter as tk

def message_to_binary(message):
    ascii_values = [] # List for ascii values
    binary_values = [] # List for final binary message

    for letter in message: # Iterates through string and applies ascii value
        ascii_values.append(ord(letter))

    for value in ascii_values: # Turns ascii to binary
        binary_values.append(bin(value)[2:])

    global msg_length
    msg_length = len(ascii_values)

    return binary_values

# Syncs binary to sound
def sync_message(message):
 

    all_notes = [] # Each individual letters notes to sort through
    binary_inds = [] # Indexes of the letters in notes_and_letters

    frequencies = [] # Frequencies that are equivalent to message

    # Finds index of the binary for the note
    for b_notes in library.notes_and_letters: # Checks each individual list for a note
        for values in library.notes_and_letters[b_notes]:
            if values in message: # Checks if the value matches in the message
                all_notes.append(b_notes)
                binary_inds.append(library.notes_and_letters[b_notes].index(values)) # Finds index of value and adds to list
    
    for name, index in zip(all_notes, binary_inds): # Creates tuples from the lists named
        frequencies.append(library.frequencies[name][index]) # Matches the list name with the needed index and stores it!


    print('all notes', all_notes)
    return print(frequencies)
