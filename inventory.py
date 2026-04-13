# Importing tabulate function for view_all()
from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    # Creating a shoe class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)
        
    # Creating a function for obtaining cost
    def get_cost(self):

        return self.cost
    # Creating a function for obtaining quantity
    def get_quantity(self):
        return self.quantity   
    # Creating a function for all displaying product info
    def __str__(self):
        return f"(Country: {self.country},     Code: {self.code},\
        Product: {self.product},     Price: {self.cost},\
        Quantity: {self.quantity})"

  #=============Shoe list===========
shoe_list = []
  #==========Functions outside the class==============  
def read_shoes_data():
    try:    # Defensive programming to avoid file errors
        with open("inventory.txt", "r") as file:
            # Skipping the first line in text file
            for i, line in enumerate(file): 


                if i == 0:
                    continue  
                line = line.strip() # Removing whitespace
                inventory=line.split(",") # Removing commas
                country, code, product, cost, quantity = inventory
                # Creating list of objects
                shoe =  Shoe(country, code, product, cost, quantity) 
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error! File not found.\n")
   

def capture_shoes():
    ''' User inputs to capture shoe data''' 
    print("--- Capturing shoe data--- ")
    country = input("Please enter country name: ")
    code = input("Please enter shoe code: ")
    product = input("Please enter the product name: ")
    while True: # Defensive programing to avoid user inputs crashing
        try:
            cost = int(input("Please enter the price: "))
            break

        except ValueError:
            print("Invalid price entered! Re-enter value.")

    while True:
        try:
            quantity = int(input("Please enter the quantity: ")) 
            break

        except ValueError:
            print("Invalid quantity entered! Re-enter value.")    

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe) # Adding items to the list

def view_all(): 
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    table_data = []
    for shoe in shoe_list:
        table_data.append([
            shoe.country,
            shoe.code,
            shoe.product,
            shoe.cost,
            shoe.quantity
        ])
    table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
    print(table)

def re_stock():
    # Finding the item with the least stock
    lowest_stock = min(shoe_list, key=lambda shoe: shoe.quantity)

    print(f"Lowest stock item:{lowest_stock}")
    # Giving user choice to add stock
    restock = input("Would you like to re-stock the shoe? Yes/No: ").lower()


    if restock == "yes":
        while True:
            try:
                restock_amnt = int(input("Enter additional quantity: "))
                lowest_stock.quantity += restock_amnt
                print(f"New stock amount:{lowest_stock.quantity}.")
                with open("inventory.txt","w") as file:
                   file.write("Country,Code,Product,Cost,Quantity \n")
                   for shoe in shoe_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},"
                               f"{shoe.cost},{shoe.quantity}\n")
                break
            except ValueError:
                print("Invalid amount entered. Re-enter value.")
    elif restock == "no":
        pass
    else:
        print("Invalid entry!")


def search_shoe():
    user_code = input("Please enter shoe code: ")

    for shoe in shoe_list:
        if shoe.code == user_code:
            print(shoe)
            return
        
    
    print("Shoe not found.")


def value_per_item():

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} is valued at: {value}")

def highest_qty():
    # Finding the highest quantity 
    highest_stock = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"Shoes available for sale:\n {highest_stock}")


#==========Main Menu=============

read_shoes_data()

while True:
    # Printing the main display options
    print("Welcome to the Store Inventory Control.")
    print("\n--- MAIN MENU ---\n")
    print("Please select a number from the menu.\n")
    print("1. Display available stock.")
    print("2. Add a new item to stock.")
    print("3. Shoe re-stock.")
    print("4. Search shoe.")
    print("5. Value per stock item.")
    print("6. Display the highest stock item.")
    print("7. To exit.")

    # User inputs a number form the options
    menu_option = input("Please enter number: ")

    if menu_option == "1":
        view_all()
    elif menu_option == "2":
        capture_shoes()
    elif menu_option == "3":
        re_stock()
    elif menu_option == "4":
        search_shoe()
    elif menu_option == "5":
        value_per_item()
    elif menu_option == "6":
        highest_qty()
    elif menu_option =="7":
        print("Exit!")
        break
    else:
        print("Invalid option.")

# Used ChatGPT for troubleshooting errors in code