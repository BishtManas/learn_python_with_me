# -------------------------------
# 1️⃣ Arithmetic Operators Example
# -------------------------------

a = 10
b = 3

print("Addition:", a + b)         # 10 + 3 = 13
print("Subtraction:", a - b)      # 10 - 3 = 7
print("Multiplication:", a * b)   # 10 * 3 = 30
print("Division:", a / b)         # 10 / 3 = 3.33 (returns float)
print("Floor Division:", a // b)  # 10 // 3 = 3 (removes decimal part)
print("Modulus (Remainder):", a % b)  # 10 % 3 = 1
print("Exponent (Power):", a ** b)    # 10 ** 3 = 1000

# -------------------------------
# 2️⃣ Assignment Operators Example
# -------------------------------

x = 5
print("\nInitial x:", x)  # Now x is equal to 5

# Run this code in your compiler to see each result step-by-step.

x += 2   # x = x + 2
print("After += 2:", x)

x *= 3   # x = x * 3
print("After *= 3:", x)

x -= 4   # x = x - 4
print("After -= 4:", x)

x /= 2   # x = x / 2
print("After /= 2:", x)  # This will give a float value

# Note: If you use '//' instead of '/', it will give an integer by removing the decimal part.

x **= 2  # x = x ** 2
print("After **= 2:", x)

# -------------------------------
# 3️⃣ Comparison Operators Example
# -------------------------------

a = 15
b = 20

# This checks if the value of 'a' is equal to 'b'. If true, returns True, else False.
print("\nIs a equal to b?", a == b)       # False

# This checks if 'a' is not equal to 'b'.
print("Is a not equal to b?", a != b)     # True

# These compare the values using greater than, less than, etc.
print("Is a greater than b?", a > b)      # False
print("Is a less than b?", a < b)         # True
print("Is a greater or equal to b?", a >= b)  # False
print("Is a less or equal to b?", a <= b)     # True

# -------------------------------
# 4️⃣ Logical Operators Example
# -------------------------------

x = 7

# 'and' checks if both conditions are True
print("\nLogical AND (x > 5 and x < 10):", x > 5 and x < 10)  # True

# 'or' returns True if any one condition is True
print("Logical OR (x < 5 or x == 7):", x < 5 or x == 7)       # True

# 'not' reverses the result. If x == 7 is True, then not True becomes False
print("Logical NOT (not x == 7):", not x == 7)                # False

# -------------------------------
# 5️⃣ Identity Operators Example
# -------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIs 'a' the same object as 'b'?", a is b)         # True (same object in memory)
print("Is 'a' the same object as 'c'?", a is c)           # False (same values but different objects)
print("Is 'a' not the same as 'c'?", a is not c)          # True

# -------------------------------
# 6️⃣ Membership Operators Example
# -------------------------------

fruits = ["apple", "banana", "cherry"]

# Checks if 'banana' is in the list
print("\nIs 'banana' in fruits?", "banana" in fruits)   # True

# Checks if 'mango' is NOT in the list
print("Is 'mango' not in fruits?", "mango" not in fruits)  # True

# -------------------------------
# 🎯 Summary
# -------------------------------
# Arithmetic → +, -, *, /, //, %, **
# Assignment → =, +=, -=, *=, /=, **=
# Comparison → ==, !=, >, <, >=, <=
# Logical → and, or, not
# Identity → is, is not
# Membership → in, not in
