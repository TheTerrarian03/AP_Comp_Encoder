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
    binary_inds = []

    for notes in library.notes_and_letters:
        for values in library.notes_and_letters[notes]:
            print(values)
            if values in message:
                print('woohoo') 
                print('value:',values,'notes:',notes)
                #binary_inds.append()
                print(library.notes_and_letters[notes.index(values)])
            else:
                print('no')

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
enter = tk.Button(msg_window, text='Enter Message', command= sync_message(binary_conversion(msg)))
enter.grid(column=6, row=7, sticky='news')

msg_window.mainloop()
