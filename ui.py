import tkinter as tk, binary_conversion
from tkinter import ttk
from tkinter import filedialog

def browse_files():
    filename = filedialog.askopenfilename(initialdir='/',title ='Select a file',filetypes=('.wav'))
    label.configure(text = filename)

# Function for button press
def encoding_button():
    return binary_conversion.sync_message(binary_conversion.message_to_binary(msg.get()))

# Funcrion for dropdown menu
def options_changed(event):
    if options.get() == 'Encode':
        return encoding_page.tkraise()
    if options.get() =='Decode':
        return decoding_page.tkraise()

root = tk.Tk()
root.wm_geometry('500x500')
root.title('Message Encoding & Decoding') 
root.configure(background= '#B2D2A4')

# A dropdown menu for navigating the ui
options_available = ['','Encode','Decode'] 

options = ttk.Combobox(root, values=options_available, state ='readonly') # Dropdown menu
options.current(0) # Sets default value to none
options.pack(padx=1,pady=1) # Places dropdown menu

options.bind('<<ComboboxSelected>>', options_changed) # Calls function to match combobox option selected to it's page
# Creates UI for inputing a message

encoding_page = tk.Frame(root) # Creates a window

# Text box for user input
msg = tk.StringVar()
msg_box = tk.Entry(encoding_page, textvariable=msg)
msg_box.grid(column=6, row=8, sticky='news')

# Enter button
enter_msg = tk.Button(encoding_page, text='Enter Message', command= encoding_button)
enter_msg.grid(column=6, row=7, sticky='news')

decoding_page = tk.Frame(root)
label = tk.Label(decoding_page, text = 'File')

# Button for selecting a file
file_select = tk.Button(decoding_page, text = 'Select file', command= browse_files)

root.mainloop()
