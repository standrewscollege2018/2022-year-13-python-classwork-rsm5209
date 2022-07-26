''' This is a Student Management System using object orientation'''

class Student:
    ''' Student objects have a name, age, phone number, enrolment status
        and a list of their classes '''

    def __init__(self, name, age, phone, classes):
        ''' Set up new student object '''

        self._name = name
        self._age = age
        self._phone = phone
        self._classes = classes
        self._enrolled = True

        # Append to student_list
        student_list.append(self)

    def get_name(self):
        ''' Return student name'''

        return self._name

    def get_age(self):
        ''' Return student age'''

        return self._age

    def get_phone(self):
        ''' Return student phone number'''

        return self._phone

    def get_enrolled(self):
        ''' Return student enrolment status'''

        return self._enrolled

    def get_classes(self):
        ''' Display a list of classes student is enrolled in '''
        class_list = ""
        for c in self._classes:
            class_list += c + " "
        return class_list
    
# List to store students
student_list = []


def display_students():
    ''' Display names of all students '''
    for s in student_list:
        print("=" * 30)
        print(f"Name: {s.get_name()}")
        print(f"Age: {s.get_age()}")
        print(f"Phone: {s.get_phone()}")
        print(f"Classes: {s.get_classes()}")
        print("=" * 30)
        print("")

def display_student(name):
    ''' Display details of selected student '''
    for s in student_list:
        if name.lower() in s.get_name().lower():
            print("=" * 30)
            print(f"Name: {s.get_name()}")
            print(f"Age: {s.get_age()}")
            print(f"Phone: {s.get_phone()}")
            print(f"Classes: {s.get_classes()}")
            print("=" * 30)
            print("")
        

def generate_students():
    ''' Import students from a csv file '''
    # Import the csv package to enable the program to work with a csv
    import csv
    # Open the csv file, call is csvfile
    with open('myRandomStudents.csv', newline='') as csvfile:
        # use the reader() function and put the results into a variable called filereader
        filereader = csv.reader(csvfile)
        # loop through the csv, one row at a time
        
        for line in filereader:
            # for each row, we grab the classes in columns D-H and put them into a list
            # the classes therefore can be found in line[3] to line[7]
            classes = []
            i = 3
            while i in range(3,8):
                # Creating a master list of all class codes
                if line[i] not in all_classes:
                    all_classes.append(line[i])
                # Add class to student list of classes
                classes.append(line[i])
                i += 1
            # Create a new student object
            Student(line[0], int(line[1]), int(line[2]), classes)
            
def class_search():
    ''' This function gets the user to enter a class code (such as MAT) and returns the names of all students enrolled in that class 
    Also returning the number of students enrolled in that class '''
    print("Select the class")
    for i in range(len(all_classes)):
        print (f"{i+1}.{all_classes[i]}")    
    selection = int(input("Class number: "))
    count = 0
    for a in student_list:
        if all_classes[selection-1] in a.get_classes():
            count += 1
            print("=" * 30)
            print(f"Name: {a.get_name()}")
            print(f"Age: {a.get_age()}")
            print(f"Phone: {a.get_phone()}")
            print(f"Classes: {a.get_classes()}")
            print("=" * 30)
            print("")
    print(f"{count} Students found\n")
    
def add_student():
    ''' function enables us to add a new student '''
    
    name = input("Name: ")
    age = int(input("Age: "))
    number = int(input("Phone Number: "))
    classes = []
    ask_class = True
    for i in range(len(all_classes)):
        print (f"{i+1}.{all_classes[i]}")    
    while ask_class == True:
        c = input("Enter class code (-1 to end): ")
        if c == "-1":
            ask_class = False
        else: 
            classes.append(c)
    Student(name, age, number, classes)

def update_student():
    ''' Choose what to update (name, age, phone), then enter the new info.
        Then call a setter function on the object itself to set the new value '''
    
    
def delete_student():
    student_name = input("Enter name of student to search: ")
    display_student(student_name)
    student_select = input("Enter full name of Student: ")
    search = True
    while search == True:
        for s in student_list:
            if student_select == s.get_name():
                index = student_list.index(s)
                student_list.pop(index)
                print(f"\nSuccess {student_select} has been deleted\n")
                search = False

    
    
    
all_classes = []
generate_students()
menu = True
while menu == True:
    print("1. Search Students \n2. Display all Students \n3. Search Students per class \n4. Add a New Student \n5. Delete a Student")
    menu_choice = int(input("Select what option you would like to do: "))
    if menu_choice == 1:
        student_name = input("Enter name of student to search: ")
        display_student(student_name)
    elif menu_choice == 2:
        display_students()
    elif menu_choice == 3:
        class_search()
    elif menu_choice == 4:
        add_student()
    elif menu_choice == 5:
        delete_student()
        

