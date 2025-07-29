## 📦 What is a **Module** in Python?

A **module** is just a **Python file** (`.py`) that contains **functions**, **classes**, or **variables** you can use in another Python file.

### ✅ Why use a module?

* To **reuse** code.
* To **organize** your code into small, manageable files.
* To **avoid writing everything** in one big file.

---

### 🧠 Simple Example:

Let’s say you have a file called: `math_tools.py`

```python
# This is a module named math_tools.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Now, in another Python file (like `main.py`), you can use this module:

```python
# This is your main.py file

import math_tools

print(math_tools.add(5, 3))       # Output: 8
print(math_tools.multiply(4, 2))  # Output: 8
```

👉 So here `math_tools` is a module that you're **importing**.

---

## 📂 What is a **Package** in Python?

A **package** is a **folder** that contains **multiple Python modules** and a special file called `__init__.py`.

### ✅ Why use a package?

* To **organize related modules together**.
* To build **large applications**.
* To make **code modular and scalable**.

---

### 📁 Example Package Structure:

```
my_package/
│
├── __init__.py           ← tells Python that this is a package
├── math_tools.py
├── string_tools.py
```

### 👉 Let’s say:

**math\_tools.py:**

```python
def add(a, b):
    return a + b
```

**string\_tools.py:**

```python
def shout(text):
    return text.upper() + "!!!"
```

Now you can use it like this:

```python
# main.py
from my_package import math_tools, string_tools

print(math_tools.add(5, 2))            # Output: 7
print(string_tools.shout("hello"))     # Output: HELLO!!!
```

---

## 💡 Summary Table:

| Term        | Meaning                                     | Example         |
| ----------- | ------------------------------------------- | --------------- |
| **Module**  | A single `.py` file                         | `math_tools.py` |
| **Package** | A folder with many `.py` files + `__init__` | `my_package/`   |

---

## 🔌 Built-in Examples:

Python already comes with built-in **modules** and **packages** like:

* **`math` module**

  ```python
  import math
  print(math.sqrt(16))  # Output: 4.0
  ```

* **`os` package** (has multiple modules to work with files)

  ```python
  import os
  print(os.getcwd())  # Shows current working directory
  ```
