import time


def user():
    users = {}
    name = input("Enter your name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter your name: ").strip()

    pin = input("Set a 4-digit PIN: ").strip()
    while not (pin.isdigit() and len(pin) == 4):
        pin = input("Invalid PIN. Enter a 4-digit numeric PIN: ").strip()

    users[name] = pin
    time.sleep(1)

    print("\nUser created successfully!\n")
    print("Account Summary")
    print("-" * 40)
    print(f"Name: {name}")
    print(f"PIN : {'*' * len(pin)}")
    print("-" * 40)

    return users


if __name__ == "__main__":
    user()