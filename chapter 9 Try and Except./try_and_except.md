# 🛡️ `try` and `except` in Python
---

## ✅ Why Do We Use `try-except`?

When your Python program runs into an error (like dividing by zero or opening a missing file), it **crashes**.

To **avoid crashing**, we use `try-except` to **handle errors** smoothly.

---

## 🧠 Basic Syntax:

```python
try:
    # code that might cause an error
except:
    # code that runs if error happens
```

---

## 💥 Example: Divide by Zero

```python
try:
    a = 5 / 0
except:
    print("Error happened! You can't divide by zero.")
```

🟢 Output:

```
Error happened! You can't divide by zero.
```

🔍 Without `try-except`, this would crash your program.

---

## 🔍 Catching Specific Errors

You can catch **specific types** of errors to make your program smarter.

```python
try:
    num = int("hello")  # trying to convert string to number
except ValueError:
    print("You gave an invalid number!")
```

🟢 Output:

```
You gave an invalid number!
```

---

## 🎯 Common Error Types

| Error Name          | Happens When...                     |
| ------------------- | ----------------------------------- |
| `ZeroDivisionError` | Dividing by 0                       |
| `ValueError`        | Invalid value (like `int("abc")`)   |
| `FileNotFoundError` | File doesn’t exist                  |
| `TypeError`         | Wrong data type in operation        |
| `IndexError`        | Accessing wrong index in list       |
| `KeyError`          | Accessing missing key in dictionary |

---

## 🧪 Multiple `except` Blocks

You can handle different types of errors **differently**:

```python
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Can't divide by zero")
```

🟢 Output:

```
Value error occurred
```

---

## 🔁 `else` with `try-except`

If no error happens, `else` block runs.

```python
try:
    print("No error here")
except:
    print("Some error")
else:
    print("Everything went well!")
```

🟢 Output:

```
No error here
Everything went well!
```

---

## 🔚 `finally` Block

Code inside `finally` **always runs**, whether there’s an error or not.

Useful for cleaning up tasks (closing file, etc.)

```python
try:
    a = 10 / 2
except:
    print("Error happened")
finally:
    print("This runs no matter what")
```

🟢 Output:

```
This runs no matter what
```

---

## 📁 Real Life Example: Reading a File

```python
try:
    f = open("data.txt")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing program.")
```

---

## 🧰 Pro Tip: `raise` Custom Error

You can manually raise errors using `raise`.

```python
age = -5

if age < 0:
    raise ValueError("Age can't be negative!")
```

---

## ✅ Summary

| Keyword   | What It Does          |
| --------- | --------------------- |
| `try`     | Code that might break |
| `except`  | Handles the error     |
| `else`    | Runs if no error      |
| `finally` | Always runs           |

---

## ✅ Practice Task for You

Try this code and change the values to test:

```python
try:
    marks = int(input("Enter your marks: "))
    print("You entered:", marks)
except ValueError:
    print("Please enter a valid number!")
finally:
    print("Input checking done.")
```
