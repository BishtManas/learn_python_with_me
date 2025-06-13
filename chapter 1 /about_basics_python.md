### 📘 `README.md` – Learn Python with Me

---

## 🚀 Getting Started with Python

This repo is made for beginners who want to learn Python from scratch. Let's start with some very basic but powerful concepts.

---

## 📢 `print()` Function

The `print()` function is used to **display output** on the screen.

### ✅ Syntax:

```python
print("Hello, World!")
```

### ✅ Quotes You Can Use:

You can use:

* Double quotes: `"Hello"`
* Single quotes: `'Hello'`
* Triple quotes for multi-line: `"""Hello"""`

```python
print("Hello")
print('Hello')
print("""This is 
a multi-line 
print""")
```

---

## 💬 Comments in Python

Comments are used to explain code. Python **ignores** them while running.

### ✅ Single-line comment:

```python
# This is a single-line comment
```

### ✅ Multi-line comment (not official, but used this way):

```python
"""
This is a multi-line
comment or docstring
"""
```

---

## 🧠 Data Types

### 1. `int` – Integer (whole numbers)

```python
a = 5
print(a)  # Output: 5
```

### 2. `str` – String (text)

```python
name = "Alice"
print(name)  # Output: Alice
```

### 3. `float` – Decimal numbers

```python
pi = 3.14
print(pi)  # Output: 3.14
```

### 4. `bool` – Boolean (True/False)

```python
is_active = True
print(is_active)  # Output: True
```

---

## ⚠️ Mixing Data Types

You **cannot add** an `int` and a `str` directly:

```python
age = 25
name = "John"
# print(age + name)  ❌ This will give an error
```

✅ Correct way:

```python
print(name + str(age))  # Output: John25. you must convert integer into string or vice versa.
```

---

## 🧾 Legal Variable Names

You can name variables using:

* Letters (a-z, A-Z)
* Numbers (but not at the beginning)
* Underscores (\_)

### ✅ Valid Names:

```python
my_var = 5
_var2 = 10
user_name = "Alice"
```

### ❌ Invalid Names:

```python
2cool = "no"       # Starts with a number ❌
my-var = "wrong"   # Hyphen not allowed ❌
class = "oops"     # 'class' is a reserved keyword because class is already a buildin function❌
```

---

## 🎯 Summary

* Use `print()` to show output
* Use `"`, `'`, and `""" """` to print strings
* Use `#` for comments
* Learn basic types: `int`, `str`, `float`, `bool`
* Don’t mix data types without converting them
* Use legal variable names
* Save your code using clear Git commit messages

