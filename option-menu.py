''' This program will demonstrate how to populate and use an option menu '''

class Item():

    def __init__(self, name, value):

        self._name = name
        self._value = value

        all_items.append(self)
   
    def get_name(self):
        ''' Return name of item '''

        return self._name

    def get_value(self):
        ''' Return value of item '''

        return self._value
    

def generate_items():
    ''' Import students from a csv file'''
    # Import the csv package to enable the program to work with a csv
    import csv
    # Open the csv file, call is csvfile
    with open('products2.csv', newline='') as csvfile:
        # use the reader() function and put the results into a variable called filereader
        filereader = csv.reader(csvfile)
        # Loop through the csv, one row at a time
        
        for line in filereader:
            # For each row, create a new item


            Item(line[0], int(line[1]))

def print_selection():
    ''' Print out the selected item ''' 
    for num in items_listbox.curselection():
        # Display name and value in a label
        details.set(f"{all_items[num].get_name()} costs ${all_items[num].get_value()}")
        
def delete_item():
    ''' Delete the selected item '''
    
    for num in items_listbox.curselection():
        item_to_delete = num
        # Check whether user actually wants to delete this item
    if messagebox.askyesno("Warning!",f"Are you sure you want to delete the {all_items[item_to_delete].get_name()}?"):               
        del all_items[item_to_delete]
        
    # Clear listbox
    items_listbox.delete(0, END)
    
    # Repopulate listbox
    populate_listbox()
        
def populate_listbox():
    # Populate listbox with names of items
    for i in all_items:
        items_listbox.insert(END, i.get_name())

def enter_item():
    
    Item(name_input.get(), int(price_input.get()))
    name_input.set("")
    price_input.set("")
    
    # Clear listbox
    items_listbox.delete(0, END)
    
    # Repopulate listbox
    populate_listbox()    
    
            
# List of all item names so we can populate the option menu
item_names = []
# List of all objects
all_items = []

# Import the items from csv file
generate_items()

# Set up the GUI
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Option menu demo")
root.geometry("800x500")

# Set up listbox
items_listbox = Listbox(root, selectmode=SINGLE)
items_listbox.grid(row=0, padx=(10, 10), pady=(10,10))
populate_listbox()

# Button to enter selection
select_btn = Button(root, text="Select", command=print_selection)
select_btn.grid(row=1)

# Label
details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=2, padx=(10, 10), pady=(10,10))

# Button for deleting selected item
delete_btn = Button(root, text="Delete", command=delete_item)
delete_btn.grid(row=1, column=1)

# Label for entry form
title_lbl = Label(root, text="Add new item")
title_lbl.grid(row=0, column=2)

# Label for Name form
name_lbl = Label(root, text="Name")
name_lbl.grid(row=1, column=2)

# Input for Name form
name_input = Entry(root)
name_input.grid(row=1, column=3)

# Label for Price form
price_lbl = Label(root, text="Price")
price_lbl.grid(row=2, column=2)

# Input for Price form
price_input= Entry(root)
price_input.grid(row=2, column=3)

# button for entry form
enter_btn = Button(root, text="Enter", command=enter_item)
enter_btn.grid(row=3, column=2)


# Launch the program
root.mainloop()