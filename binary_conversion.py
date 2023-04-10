import library

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

    for val in message: # val is each individual binary that makes up the message
        for notes in library.notes_and_letters: # Checks each note and then each binary inside note
            for values in library.notes_and_letters[notes]:
                if val == values: # Matches values
                    all_notes.append(notes)
                    binary_inds.append(library.notes_and_letters[notes].index(values)) # Finds the index of values and matches a frequency

    for name, index in zip(all_notes, binary_inds): # Creates tuples from the lists named
        frequencies.append(library.frequencies[name][index]) # Matches the list name with the needed index and stores it!

    return print(frequencies)
