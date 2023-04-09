import tkinter as tk, binary_conversion
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.wm_geometry('500x200')
root.title('Message Encoding & Decoding') 
root.configure(background= '#B2D2A4')

start_page = tk.Frame(root)
start_page.grid(column=0, row=0, sticky='news')

decoding_page = tk.Frame(root)
decoding_page.grid(column=0, row=0, sticky='news')

encoding_page = tk.Frame(root)
encoding_page.grid(column= 0, row=0, sticky='news')

def back_buttons():
    return(start_page.tkraise())

# Allows user to select file
def browse_files():
    filename = filedialog.askopenfilename(initialdir='/',title ='Select a file',filetypes=(('Wavio files','*.wav*'),('all files', '*.*'))) # Should open file explorer
    file_name.configure(text = filename) # Changes label so user can see the file they selected

# Function for enter button on encoding page
def encoding_button():
    return(binary_conversion.sync_message(binary_conversion.message_to_binary(msg.get())))

# Function for button on start page
def enter_button():
    return(options.bind('<<ComboboxSelected>>', options_changed)) # Calls function to match combobox option selected to it's page

# Function for dropdown menu on start page
def options_changed(event):
    if options.get() == 'Encode':
        print('encode')
        return(encoding_page.tkraise())
    elif options.get() == 'Decode':
        print('decode')
        return(decoding_page.tkraise())

# - Start Page -
start_page.tkraise()
options_available = ['','Encode','Decode'] # Options available

options = ttk.Combobox(start_page, values=options_available, state ='readonly') # Dropdown menu
options.current(0) # Sets default value to none
options.grid(column=4,row=1, sticky = 'news') # Places dropdown menu

enter_choice = tk.Button(start_page, text = 'Goto', command = enter_button) # Checks value in dropdown menu
enter_choice.grid(column=4, row=2, sticky = 'news')

# - Decoding Page -
file_name = tk.Label(decoding_page, text = '(file name here)') # Label for file name
file_name.grid(column=4,row=1,sticky= 'news')

file_select = tk.Button(decoding_page, text = 'Select file', command= browse_files) # Button for selecting file
file_select.grid(column=4, row=2, sticky='news')

back_button1 = tk.Button(decoding_page, text ='Back', command=back_buttons) # Takes you back to start page
back_button1.grid(column=4, row=4)

# - Encoding Page -
msg = tk.StringVar() # Text box for user input
msg_box = tk.Entry(encoding_page, textvariable=msg)
msg_box.grid(column=4, row=1, sticky='news')

enter_msg = tk.Button(encoding_page, text='Enter Message', command= encoding_button) # Enter button
enter_msg.grid(column=4, row=2, sticky='news')

back_button2 = tk.Button(encoding_page, text= 'Back', command= back_buttons) # Takes you back to start page
back_button2.grid(column=4, row=4, sticky='news')

root.mainloop()