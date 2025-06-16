# Chapter 2

## 🧠 Python Basics - Notes on Input, Variables, and f-strings

---

### 📥 1. Taking Input from the User

#### ➤ Basic input:

```python
name = input("Enter your name: ")
print("Hello", name)
```

* `input()` is used to take input from the user.
* Whatever you type is always treated as a **string** (text) by default.

#### ➤ Want a number instead of text? Use `int()` or `float()` to convert:

```python
age = int(input("Enter your age: "))   # Converts input to integer
height = float(input("Enter height: ")) # Converts input to float
```

---

### 🔤 2. Data Types in Python

#### ➤ What is a variable?

A variable is like a container. You give it a name, and it stores some data.

---

### 🔢 3. Types of Variables (Data Types)

| Data Type | Python Keyword | Example         | Description                        |
| --------- | -------------- | --------------- | ---------------------------------- |
| Integer   | `int`          | `5`, `100`      | Whole numbers, no decimal          |
| Float     | `float`        | `5.5`, `3.14`   | Numbers with decimal point         |
| String    | `str`          | `"hello"`       | Text values                        |
| Boolean   | `bool`         | `True`, `False` | True/False values (yes/no, on/off) |

---

### ✅ 4. Examples

```python
# Integer
apples = 10
print(type(apples))  # Output: <class 'int'>

# Float
price = 49.99
print(type(price))   # Output: <class 'float'>

# String
city = "Delhi"
print(type(city))    # Output: <class 'str'>

# Boolean
is_day = True
print(type(is_day))  # Output: <class 'bool'>
```

---

### 🔍 5. Where do we use these?

* `int`: Age, score, quantity → `score = 50`
* `float`: Money, height, temperature → `temp = 37.5`
* `str`: Names, places, text messages → `username = "Sir"`
* `bool`: Yes/No checks, logic → `is_active = False`

---

### ✨ 6. f-string (formatted strings)

#### ➤ What is an `f-string`?

It's a way to include variables **inside** your print statements **without** using commas or `+` signs.

#### ➤ Old way:

```python
name = "Sir"
print("Hello " + name)
```

#### ➤ New and better way (f-string):

```python
name = "Sir"
print(f"Hello {name}")
```

#### ➤ Why use f-strings?

* Clean syntax
* Easy to write and read
* You can even do **math** inside:

```python
price = 100
discount = 20
print(f"Final price: {price - discount}")   # Output: Final price: 80
```

#### ➤ Multiple variables:

```python
name = "Sir"
age = 18
city = "Mumbai"

print(f"My name is {name}, I am {age} years old and I live in {city}.")
```

---

### 🔧 7. Practice Code (All Together Now)

```python
# Take user input
name = input("What is your name? ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
is_student = True  # Assume he is a student

# Print everything using f-string
print(f"\nHello {name}!")
print(f"You are {age} years old.")
print(f"Your height is {height} cm.")
print(f"Are you a student? {is_student}")# Try yourself 
```

---

### 💡 8. Important Points to Remember

* Use `input()` for user input. Use `int()` or `float()` to convert it.
* Variables can change. That’s why they are called “variables.”
* `f-strings` make output look professional and clean.
* Use `type()` to check what type of variable you have.