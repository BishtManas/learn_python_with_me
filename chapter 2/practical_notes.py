# ---------------------------------------
# 🐍 Python Basics: Input and Variables
# ---------------------------------------

# 💬 Example 1: Taking a simple input

name = input("What is your name? ")  # input() takes string input from user
print("Hello", name)  # Output: Hello <name>

# 🧠 input() always returns a string
# If you need a number, you must convert it

# 💬 Example 2: Taking integer input

age = int(input("Enter your age: "))  # Converts input string to integer
print("Your age is:", age)

# 💬 Example 3: Taking float input (decimal)

height = float(input("Enter your height in cm: "))  # Converts input to float
print("Your height is:", height, "cm")

# ---------------------------------------
# 🔢 Variable Types (Data Types)
# ---------------------------------------

# 💡 Integers

num_apples = 5
print("Number of apples:", num_apples)
print("Data type of num_apples:", type(num_apples))  # Output: <class 'int'>

# 💡 Floats

price = 49.99
print("Price:", price)
print("Data type of price:", type(price))  # Output: <class 'float'>

# 💡 Strings

city = "Mumbai"
print("City:", city)
print("Data type of city:", type(city))  # Output: <class 'str'>

# 💡 Booleans

is_raining = False
print("Is it raining?", is_raining)
print("Data type of is_raining:", type(is_raining))  # Output: <class 'bool'>

# ---------------------------------------
# 🎯 Real Use Case (Mixing inputs)
# ---------------------------------------

# Taking all types of input and showing them with f-strings

username = input("Enter your username: ")
user_age = int(input("Enter your age: "))
user_height = float(input("Enter your height in cm: "))
is_student = True  # Let's assume the user is a student

# Using f-string to display all info in one line (clean and easy)

print(f"\nHello {username}! You are {user_age} years old, {user_height} cm tall.")
print(f"Are you a student? {is_student}")

# ---------------------------------------
# ✨ f-Strings Explained with Examples
# ---------------------------------------

# 💬 Example 1: Simple usage

fruit = "Mango"
print(f"I like {fruit}")  # Output: I like Mango

# 💬 Example 2: Doing math inside f-string

price = 100
discount = 20
print(f"Discounted price: {price - discount}")  # Output: Discounted price: 80

# 💬 Example 3: Multiple variables

first_name = "John"
last_name = "Doe"
print(f"Full name: {first_name} {last_name}")  # Output: Full name: John Doe
# If you want to print input in inside of your quotes then you can use "f" string method.

# 💬 Example 4: Formatting float value to 2 decimal places

pi = 3.1415926535
print(f"Value of pi: {pi:.2f}")  # Output: Value of pi: 3.14
# You can also formate decimal with your choice like you want 3 decimal just type .3f.

# ---------------------------------------
# 🚀 End of Notes
# ---------------------------------------

# ✨ Summary:
# - Use input() to take user input
# - Convert input using int(), float() when needed
# - Use type() to check data types
# - Use f-strings for clean and dynamic output
