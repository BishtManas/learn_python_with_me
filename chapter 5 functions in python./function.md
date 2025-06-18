# 📦 Python Functions – Full Beginner Guide

---

## 🔷 What is a Function?

A **function** is like a mini-program inside your main program.
You can write a block of code, give it a name, and run it whenever you want — without repeating code.

### ✅ Why use functions?

* To **reuse code**.
* To make your code **organized and clean**.
* To **avoid repeating yourself**.

---

## 🔹 How to Create a Function?

In Python, we create a function using the `def` keyword.

```python
def function_name():#you can give any name to your function.

    # Code block (this is called the function body)
    print("Hello from the function!")
```

### 📞 How to call a function?

Just use its name followed by parentheses `()`

```python
function_name()
```

---

## 🔹 Function with Parameters

A function can take **inputs**. These inputs are called **parameters**.

```python
def greet(name):# name is a parameter.
    print("Hello", name)
    
greet("Sir")# you can type any name as you want and you can also call this function again.

greet("snail")#you can also change name.

# first output : Hello sir
# second output : Hello snail
```

---

## 🔹 Function with Return Value

You can also make a function **give you back a result** using the `return` keyword.

```python
def add(a, b):
    return a + b# return just give you a value like in this case return give a + b but if you see the results you must be print this function.

result = add(3, 5)
print(result)# In this case we print the function because return only give value.
# Output: 8
```

> `return` sends a value back to the place where the function was called.

---

## 🔹 Default Parameter Values

You can give default values to parameters. If no value is given when calling, it uses the default.

```python
def greet(name="Guest"):# If you didn't pass any value in name the function automatically pass name as Guest.

# But if you pass name then the name is now as you pass.

    print("Hello", name)

greet()        # Hello Guest
greet("Snail") # Hello Snail
```

---

## 🔹 Keyword Arguments

You can pass arguments using `key=value` style.

```python
def student(name, age):
    print(name, "is", age, "years old")

student(age=18, name="Rahul")  # Order doesn't matter now
```

---

## 🔹 \*args (Multiple Positional Arguments)

If you want to pass **many values** but you're not sure how many — use `*args`.

```python
def total_marks(*marks):# you want to pass many value and you don't know how many value you want to pass so in this case you can use args"*" at starting of the parameter.

    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(80, 85, 90)
```

> `*args` collects values into a **tuple**.

---

## 🔹 \*\*kwargs (Multiple Keyword Arguments)

If you're passing many key-value pairs, use `**kwargs`.

```python
def show_profile(**details):
    for key, value in details.items():
        print(key, ":", value)

show_profile(name="Manas", age=22, course="Python")

#output:-
# name : Manas
# age : 22
# course : Python
```

> `**kwargs` collects values into a **dictionary**.

---

## 🔹 Built-in vs User-defined Functions

| Type         | Example                          |
| ------------ | -------------------------------- |
| Built-in     | `print()`, `len()`, `sum()`      |
| User-defined | Functions you create using `def` |

---

## 🔹 Lambda Function (One-liner Function)

A **lambda** is a short one-line function.

```python
# Normal way
def square(x):
    return x * x

# Lambda way
square = lambda x: x * x
print(square(5))  # Output: 25
```

> Useful when you want quick simple function.

---

## ✅ Summary Table

| Concept                 | Example                    |
| ----------------------- | -------------------------- |
| Define a function       | `def greet():`             |
| Call a function         | `greet()`                  |
| With parameter          | `def greet(name):`         |
| Return a value          | `return a + b`             |
| Default arguments       | `def greet(name="Guest"):` |
| Keyword arguments       | `greet(name="Snail")`      |
| `*args` (many values)   | `def total(*marks):`       |
| `**kwargs` (key-values) | `def profile(**info):`     |
| Lambda function         | `lambda x: x + 1`          |
