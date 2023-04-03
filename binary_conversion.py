import library, tkinter as tk

def binary_conversion(message):
    ascii_values = [] # List for ascii values
    binary_values = [] # List for final binary message

    message_length = 0

    for letter in message: # Iterates through string and applies ascii value
        ascii_values.append(ord(letter))

    for value in ascii_values: # Turns ascii to binary
        binary_values.append(bin(value)[2:])

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
    
    return frequencies     

# Function for button press
def button_ui():
    print(sync_message(binary_conversion(msg.get())))
    return sync_message(binary_conversion(msg.get()))

# Creates UI for inputing a message
msg_window = tk.Tk() # Creates a window
msg_window.wm_geometry('500x500')
msg_window.title('Message Encoder') 
msg_window.configure(background= '#B2D2A4')

# Text box for user input
msg = tk.StringVar()
msg_box = tk.Entry(msg_window, textvariable=msg)
msg_box.grid(column=6, row=8, sticky='news')

# Enter button
enter = tk.Button(msg_window, text='Enter Message', command= button_ui)
enter.grid(column=6, row=7, sticky='news')

msg_window.mainloop()
