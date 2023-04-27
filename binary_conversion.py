import library

def message_to_binary(message):
    ascii_values = [] # List for ascii values
    binary_values = [] # List for final binary message

    for letter in message: # Iterates through string and applies ascii value
        ascii_values.append(ord(letter))

    for value in ascii_values: # Turns ascii to binary
        binary_values.append(bin(value)[2:])

    return binary_values

# Syncs binary to sound
def sync_message(message):
    all_notes = [] # Each individual letters notes to sort through
    binary_inds = [] # Indices of the letters in notes_and_letters

    frequencies = [] # Frequencies that are equivalent to message

    for val in message: # val is each individual binary that makes up the message
        for notes in library.notes_and_letters: # Checks each note and then each binary inside note
            for values in library.notes_and_letters[notes]:
                if val == values: # Matches values
                    all_notes.append(notes)
                    binary_inds.append(library.notes_and_letters[notes].index(values)) # Finds the index of values and matches a frequency

    for name, index in zip(all_notes, binary_inds): # Creates tuples from the lists named
        frequencies.append(library.frequencies[name][index]) # Matches the list name with the needed index and stores it!

    return frequencies

def frequency_undo(frequency):
    all_notes = [] # Notes that each frequency is found out
    frequency_inds = [] # Indices of each individual frequency

    binary_msg = [] # Message in binary
    ascii_msg = [] # Message in ascii 

    decoded_msg = [] # Decoded values

    for val in frequency: # Val is specific frequency
        for notes in library.frequencies: # Notes in the library of frequencies
            for freq in library.frequencies[notes]:
                if val == freq:
                    all_notes.append(notes)
                    frequency_inds.append(library.frequencies[notes].index(freq))
    
    # Finds binary value based on note and index
    for name, index in zip(all_notes, frequency_inds):
        binary_msg.append(library.notes_and_letters[name][index])

    # Converts binary to ascii value
    for binary in binary_msg:
        ascii_msg.append(int(str(binary), 2))

    # Converts ascii value to character
    for ascii in ascii_msg:
        decoded_msg.append(chr(ascii))

    # Changes the message from list to a string
    msg = ''.join([str(elem) for elem in decoded_msg])

    print(msg)
    return msg
