''' This program will demonstrate how to populate and use an option menu '''

class Item():

    def __init__(self, name, value):

        self._name = name
        self._value = value

        all_items.append(self)

        # Append name to item_names list
        item_names.append(name)

   
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

def display_selection():
    ''' Get the selected item from the option menu and display details in a list '''
    
    # Loop through all items until we find the one we selected, and get the value
    for i in all_items:
        if i.get_name() == selected_item.get():
            value = i.get_value()
    
    details.set(f"{selected_item.get()} costs ${value}")
    

# List of all item names so we can populate the option menu
item_names = []
# List of all objects
all_items = []

# Import the items from csv file
generate_items()

# Set up the GUI
from tkinter import *
root = Tk()
root.title("Option menu demo")
root.geometry("800x500")

# Option menu
# Set up a variable to store the selection
selected_item = StringVar()
# Set default value of selection
selected_item.set(item_names[0])

names_menu = OptionMenu(root, selected_item, *item_names)
names_menu.config(fg='white', width=20, height=2)
names_menu.grid(row=0, padx=(100, 10))

''' Add a button that gets the selected item, then displays the price in a label'''
# Button
select_btn = Button(root, text="Select", command=display_selection, width=20)
select_btn.grid(row=1, column=0, padx=(100, 10))
# Label
details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=1, column=1, padx=(100, 10))


# Launch the program
root.mainloop()

