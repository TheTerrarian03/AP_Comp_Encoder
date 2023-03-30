import library, tkinter as tk

def binary_conversion(message):
    ascii_values = [] # List for ascii values
    binary_values = [] # List for final binary message

    for letter in message: # Iterates through string and applies ascii value
        ascii_values.append(ord(letter))

    for value in ascii_values: # Turns ascii to binary
        binary_values.append(bin(value)[2:])

    return binary_values

# Syncs binary to sound
def sync_message(message):
    all_notes = [] # Each individual letters notes to sort throut
    binary_inds = [] # Indexes of the letters in notes_and_letters

    # Finds index of the binary for the note
    for notes in library.notes_and_letters: # Checks each individual list for a note
        for values in library.notes_and_letters[notes]:
            if values in message: # Checks if the value matches in the message
                all_notes.append(notes)
                binary_inds.append(library.notes_and_letters[notes].index(values)) # Finds index of value and adds to list
            else:
                print('!')

# Function for button press
def button_ui():
    return sync_message(binary_conversion(msg))

# Creates UI for inputing a message
msg_window = tk.Tk() # Creates a window
msg_window.wm_geometry('500x500')
msg_window.title('Message Encoder') 
msg_window.configure(background= '#B2D2A4')

# Text box for user input
msg = 'M'
msg_box = tk.Entry(msg_window, textvariable=msg)
msg_box.grid(column=6, row=8, sticky='news')

# Enter button
enter = tk.Button(msg_window, text='Enter Message', command= button_ui)
enter.grid(column=6, row=7, sticky='news')

msg_window.mainloop()
