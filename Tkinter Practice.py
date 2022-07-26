''' introduction to tkinter ''' 

# Import tkinter
from tkinter import *

def say_hello():
    # Change the message variable to Hello
    if message.get() == "Hello there!":
        message.set("")
    else:
        message.set("Hello there!")

# Set up the root window
root = Tk()
root.title("My first Tkinter GUI")
root.resizable(width=FALSE, height=FALSE)
root.geometry("800x500")
root.configure()

# Add a label
heading_lbl = Label(root, text="A great GUI", fg="white")
heading_lbl.grid(row=0, column=0)

# Set up label to display hello from say_hello function
# Set up a StringVar to store the text for the label
message = StringVar()
message_lbl = Label(root, textvariable=message)
message_lbl.grid(row=1, column=1)

# Add a button
pushme_btn = Button(root, text="Push me!", command=say_hello)
pushme_btn.grid(row=1, column=0)

# Start the program by running the GUI
root.mainloop()