import time
def greet():
    print("Welcome User!")

greet()

def user():
    print("Are you a new user or existing user?")
    a = input("1. New User \n 2. Existing User \n Enter your choice (1/2): ")

    if a == "1":
        name = input("Enter your name: ")
        print(f"Welcome {name}, your account has been created successfully.")
        print("Create a PIN for your account.")
        pin = input("Enter a 4-digit PIN: ")
        print("Your account has been created successfully. Please remember your PIN for future transactions.")

    elif a == "2":
        pin = input("Enter your 4-digit PIN: ")
        print("PIN verified successfully. You can now perform transactions.")
    else:
        print("Invalid choice. Please try again.")
user()


def operation():
    print("What operation would you like to perdform?.:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        withdraw()
    elif choice == "2":
        deposit()
    elif choice == "3":
        check_balance()
    else:
        print("Invalid choice. Please try again.")
operation()


def withdraw():
    amount = float(input("Enter the amount to withdraw.:"))
    print("Your request is in process. please wait....")
    time.sleep(3)
    print("Please collect your cash")
    time.sleep(3)
    print("Thank you for using our ATM service.")

def deposit():
    amount = float(input("Enter the amount to deposit.:"))
    print("Your request is in process. please wait....")
    time.sleep(3)
    print("Your amount has been deposited successfully.")
    time.sleep(3)
    print("Thank you for using our ATM service.")
