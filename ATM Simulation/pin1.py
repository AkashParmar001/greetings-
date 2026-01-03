user = {}
name = input("Enter your name.:")
pin = input("Set your 4-digit PIN.:")
user.update({name: pin})
for name, pin in user.items():
    print(name, pin)