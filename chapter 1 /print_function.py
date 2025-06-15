# -----------------------------------------------
# Topic: print() Function in Python (Beginner)
# -----------------------------------------------

# The print() function is used to display messages on the screen (output in terminal).
# You can print text, numbers, or even results of calculations.

# Example 1: Printing text (called a string)

print("Hello, world!")  # This will show: Hello, world!

# Example 2: Printing numbers

print(10)  # This will show: 10

# Example 3: Printing the result of a calculation

print(5 + 3)  # This will show: 8 (because 5 + 3 = 8)

# Example 4: Printing multiple things at once

print("My age is", 18)  

# Output: My age is 18
# Python adds a space between items by default when printing multiple items

# Example 5: Printing using variables

name = "Sir" # This is variable 
age = 18 # This is also a variable 

print("My name is", name, "and I am", age, "years old.")

# Output: My name is Sir and I am 18 years old.

# Output: This is line one | This is line two

# ----------------------------
# Escape characters in print
# ----------------------------

# \n -> new line
print("First line\nSecond line")

# \t -> tab (space)

print("Name:\tSir")

# ----------------------------
# Blank print() just adds a new line
# ----------------------------

print()  # This just prints an empty line

# ----------------------------
# Final example (summary)
# ----------------------------
print("Summary:")
print("Name:", name)
print("Age:", age)
print("Learning: Python Basics")

# You can't add directly two different variables like (string + integer) is not possible.
# Example 
a = 12 
b = "Manas"
print(a + b)# This will give an error

# You must change the type of variable 

c = str(a)
print(a + c)# Now you can add.

# output >> 12Manas