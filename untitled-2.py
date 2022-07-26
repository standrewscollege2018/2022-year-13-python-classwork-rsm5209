""" This program is a pizza ordering system for Papas Pizzaria where the phone operator can enter customer orders - Riley Smith"""

# *** Define Functions ***
def print_pizza():
    """ Prints out the list of pizzas with their price """
    print("Pizza Menu")
    # prints pizza menu
    for i in range(0, len(pizza)):
        print("{}. {}, Price ${}".format(i+1, pizza[i][0], pizza[i][1]))

def print_details():
    """ Prints order details """
    print("Details)")
    # prints out customer details
    for i in range(0, len(details)):
        print("Name) {}\nOrder Type) {}\nAddress) {}\nPhone Number) {}\n".format(details[i][1], details[i][0], details[i][2], details[i][3])) 

    
def customer_details(current_order_type, current_name, current_address, current_phone_number):
    """ Adds the Delivery Customers details to a list """
    if current_order_type == 1:
        # adds Delivery or pickup in place of numbers
        order_type = "Delivery"
    else:
        order_type = "Pickup"
    details.append([order_type, name, address, phone_number])
    
def check_login(current_system):
    """ Check if login is correct to be able to edit Menu """
    check_login = True
    # sets password as a constant
    PASSWORD = "admin"
    while check_login == True:
        # asks for password
        password = input("Enter the password to access this area\n>>> ")
        # checks if password is correct
        if password == PASSWORD:
            # returns true so while loop runs
            system_login = True
            return system_login
        else:
            print("Incorrect")
            check_login = False
    
def get_pizza_order(CURRENT_DELIVERY_PRICE):
    """ Lets the user enter orders for the customer and also prints out the entered order """
    # so while loop runs
    get_order = True
    while get_order == True:
        # reset total price
        total_price = 0
        # reset pizza amount
        pizza_amount = 0
        # prints pizza menu and asks user for how many pizzas the customer wants
        for i in range(0, len(pizza)):
            # if user enters invalid input
            try:
                print("{}. {}, Price ${}".format(i+1, pizza[i][0], pizza[i][1]))
                amount = int(input("How many {} would the customer like?\n>>> ".format(pizza[i][0])))
                # does math to get pizza price
                individual_price = amount * pizza[i][1]
                # gets total pizza amount
                pizza_amount += amount
                # gets total price using math
                total_price += individual_price
                # adds to list
                order.append([pizza[i][0], amount, individual_price])
            except:
                print("Please enter a valid input")
            # if user enters 0 pizzas then error will print
        if not pizza_amount > 0:
            print("Please enter the order again")
        else:
            # prints order confirmation with details
            print("\nOrder Confirmation:")
            print_details()
            for i in range(0, len(order)):
                if order[i][1] > 0:
                    print("{}, Amount: {}, Price:${} \n".format(order[i][0], order[i][1], order[i][2]))
            if details[0][0] == "Delivery":
                total_price += DELIVERY_PRICE
                print("Delivery Fee: $3")
            print("Total Price: ${}".format(total_price))
            get_order = False

# *** Define Lists ***
# list of pizza names and prices
pizza = [["Hawaiian Pizza", 9], ["Vege-Delite Pizza", 9], ["Meatlovers Pizza", 9], ["Pepperoni Pizza", 9], ["Margherita Pizza", 9], ["White Pizza", 9],
         ["Deep Dish Pizza", 9], ["Nutella Dessert Pizza", 9], ["Hot Dog Pizza", 9], ["Avocado and Goat Cheese Pizza", 9]]
# list for customer details
details = []
# list for customer orders
order = []

# *** Define Constants ***
DELIVERY_PRICE = 3
ACCEPTABLE_NAME_CHARACTERS = set("abcdefghijklmnopqrstuvwxyz")

# *** Defining variables ***
run_program = True
get_order = True
system = False

# *** Main Code ***
while run_program == True:
    try:
        # asks user what they want to do
        main_menu = int(input("\nWhat would you like to do? \n1) Accept an Order \n2) Edit the Menu\n3) Exit\n>>> "))
        if main_menu == 1:
            # sets as true so while loop will run
            get_details = True
            while get_details == True:
                get_name = True
                # asks for customer order details
                # error catching for name
                while get_name == True:
                    name = input("Enter the Customers First name\n>>> ")
                    # Checks for acceptable characters
                    if any((c in ACCEPTABLE_NAME_CHARACTERS) for c in name.lower()):
                        get_name = False
                    else:
                        print("Please enter a valid name")

                order_type = int(input("Choose the order type \n1) Delivery \n2) Pickup\n>>> "))
                if order_type == 1:
                    # asks for customer address and phone number for delivery
                    address = input("Enter the Customers Address\n>>> ")
                    phone_number = int(input("Enter the Customers Phone Number\n>>> "))
                    # gets out of the run_order while loop
                    get_order = True
                    get_details = False

                elif order_type == 2:
                    # as there is no address needed it is marked as 'n/a'
                    address = "n/a"
                    # gets customers phone number
                    phone_number = int(input("Enter the Customers Phone Number\n>>> "))
                    # gets out of the run_order while loop
                    get_order = True
                    get_details = False

                else:
                    # if user enters incorrect input
                    print("Please enter a valid answer")

            # runs user inputs through function to add to a list
            customer_details(order_type, name, address, phone_number)
            print("Thank you, taking you to Order Page\n")

            while get_order == True:
                # gets pizza order from user
                get_pizza_order(DELIVERY_PRICE)
                # asks if user wants to confirm order
                confirm_order = int(input("Confirm this Order\n1) Yes\n2) No\n>>> "))
                if confirm_order == 1:
                    # confirmation message
                    print("Thank you for the Order! It'll be with the Customer soon.")
                    # clears all lists for new order
                    order.clear()
                    details.clear()
                    get_order = False

                elif confirm_order == 2:
                    # if user does not confirm message
                    print("Ok, maybe next time")
                    # clears all lists for new order
                    order.clear()
                    details.clear()
                    get_order = False

                else:
                    order.clear()
                    print("Please enter a valid input")

        elif main_menu == 2:
                # Checks if user got password correct
                system = check_login(system)
                if system == True:
                    # sets as true so while loop will run
                    while system == True:
                        try:
                            edit_choice = int(input("\nSelect your option:\n1) Add a Pizza \n2) Edit a Pizza \n3) Delete a Pizza\n4) Back to Main Menu\n>>> "))
                            if edit_choice == 1:
                                get_pizza = True
                                # gathers information for new pizza
                                while get_pizza == True:
                                    # Get name of new pizza
                                    pizza_name = input("What is the name of the Pizza?\n>>> ")
                                    # checks if pizza has correct type of name
                                    if any((c in ACCEPTABLE_NAME_CHARACTERS) for c in pizza_name.lower()):
                                        get_pizza = False
                                    else:
                                        print("Please enter a valid name")
                                pizza_price = int(input("What is the price of the Pizza?\n>>> "))
                                # adds new pizza to the menu
                                pizza.append([pizza_name, pizza_price])

                            elif edit_choice == 2:
                                # asks user what name is and price
                                new_pizza = input("What is the new Pizza name?\n>>> ")
                                new_pizza_price = int(input("What is the price of the Pizza\n>>> "))
                                print_pizza()
                                # asks what pizza they want to edit
                                pizza_id = int(input("What Pizza would you like this to be applied to?\n>>> "))
                                # changes names and prices in list
                                pizza[pizza_id - 1][0] = new_pizza
                                pizza[pizza_id-1][1] = new_pizza_price

                            elif edit_choice == 3:
                                print_pizza()
                                # gathers information to delete pizza
                                delete_pizza = int(input("Choose what pizza you would like to delete\n>>> "))
                                # deletes pizza from the menu
                                del pizza[delete_pizza-1]

                            elif edit_choice == 4:
                                # exits out of the code
                                system = False

                            else:
                                # error catching
                                print("Please enter a valid input")
                        except:
                            # error catching
                            print("Please enter a valid input")
                else:
                    # if user gets password wrong
                    print("Go Back to Work!")


        elif main_menu == 3:
            # exit message
            print("Thank you for Working at Papas Pizzaria!")
            run_program = False
        else:
            #Error catching
            print("Please enter a valid input")
    except:
        # end of try except
        print("Please enter a valid input")
