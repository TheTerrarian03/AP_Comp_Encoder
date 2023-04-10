import tkinter as tk, binary_conversion, decode
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

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


def file_decoding():
    # get text property of file_name label
    filename = file_name.cget("text")
    # get frequencies
    frequencies = decode.decode(filename)

    # convert to letters

    # show popup box
    messagebox.showinfo("Decoded Message!", "Your message is:\n\n" + "aaaaa")

def back_buttons(): # Sends user back to start page
    return(start_page.tkraise())

# Allows user to select file
def browse_files():
    filename = filedialog.askopenfilename(initialdir='/',title ='Select a file',filetypes=(('Wave Files','*.wav'),('All Files', '*.*'))) # Should open file explorer
    # initialdir could also be '~' to open current directory
    file_name.configure(text = filename) # Changes label so user can see the file they selected

# Function for enter button on encoding page
def encoding_button():
    return(binary_conversion.sync_message(binary_conversion.message_to_binary(msg.get())))

# Function for dropdown menu on start page
def options_changed(event):
    if options.get() == 'Encode':
        return(encoding_page.tkraise())
    elif options.get() == 'Decode':
        return(decoding_page.tkraise())

# - Start Page -
start_page.tkraise()
options_available = ['','Encode','Decode'] # Options available

options = ttk.Combobox(start_page, values=options_available, state ='readonly') # Dropdown menu
options.current(0) # Sets default value to none
options.grid(column=4,row=1, sticky = 'news') # Places dropdown menu

options.bind('<<ComboboxSelected>>', options_changed) # Matches combobox option selected to it's page

# - Decoding Page -
file_name = tk.Label(decoding_page, text = '(file name here)') # Label for file name
file_name.grid(column=4,row=1,sticky= 'news')

file_select = tk.Button(decoding_page, text = 'Select file', command= browse_files) # Button for selecting file
file_select.grid(column=4, row=2, sticky='news')

enter_file = tk.Button(decoding_page, text ='Enter', command= file_decoding) # Button for sending file to decoding
enter_file.grid(column=4,row=3)

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