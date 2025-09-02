import random
import string

def generate_password(length, choice):
    if choice == "number":
        characters = string.digits
    elif choice == "string":
        characters = string.ascii_letters
    elif choice == "both":
        characters = string.ascii_letters + string.digits
    else:
        print("Invalid choice! Please enter 'number', 'string', or 'both'.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the length of the password: "))
    choice = input("What type of password do you want? (number / string / both): ").lower()
    
    password = generate_password(length, choice)
    if password:
        print("Your generated password is:", password)
except ValueError:
    print("Please enter a valid number for password length.")