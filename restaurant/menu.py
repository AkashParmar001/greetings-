#This code contains the menu of the restaurant
menu = {

}

print("Welcome to the Restaurant Management Menu!")
print("Follww the iinstructions to manage the restaurant menu.")
print("1. Add a new item to the menu:")
print("2. Update an existing item in the menu:")
print("3. Delete an item from the menu:")
print("4. View the menu:")
print("5. Exit the menu management system:")
while True:
    choice1 = int(input("Enter your choice (1-5): "))
    if choice1 == "5":
        print("Thank you for using the restaurant management system.")
        break
    elif choice1 == 1:
        # Add a new item to the menu
        while True:
            item_name = input("Enter the name of the item to be added to the menu: ")
            if item_name in menu:
                print(f"{item_name} is already in the menu.")
            else:
                price = int(input(f"Enter the price of {item_name}: "))
                menu[item_name] = price
                print(f"{item_name} has been added to the menu with a price of {price}.")
                break
        choice2 = input("Do you want to add a new item to the menu? (yes/no): ").lower().strip()
        if choice2 == "yes":
            print("Follow the instruction to add a new item to the menu.")
            a = input("Enter the name of the item to be add to the menu.:")
            b = int(input("Enter the price of the item to be added to the menu.:"))
            menu.update({a : b})
            print(f"{a} has been added to the menu with a price of {b}.")
