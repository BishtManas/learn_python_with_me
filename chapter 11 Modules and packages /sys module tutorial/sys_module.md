# 🧠 Python `sys` Module

The `sys` module in Python provides access to **some variables and functions** that interact directly with the **Python interpreter**.

You can think of it as a way to talk to Python itself — like getting info about your Python version, system, or changing how your program runs.

---

## 🔹 How to Import `sys` Module

```python
import sys
```

Once imported, you can use all the `sys` module functions and variables.

---

## 🧩 Common Uses of `sys` Module (Beginner-Friendly List)

| Feature           | Description                           |
| ----------------- | ------------------------------------- |
| `sys.version`     | Check Python version                  |
| `sys.argv`        | Read command-line arguments           |
| `sys.exit()`      | Exit the program manually             |
| `sys.path`        | Check Python’s module search path     |
| `sys.platform`    | Info about the OS (Windows/Linux/Mac) |
| `sys.stdin`       | Input stream                          |
| `sys.stdout`      | Output stream                         |
| `sys.stderr`      | Error output stream                   |
| `sys.getsizeof()` | Size of object in bytes               |

---

## ✅ 1. `sys.version` — Get Python Version

```python
import sys
print("Python version:", sys.version)
```

🔹 This shows which version of Python is running.

---

## ✅ 2. `sys.argv` — Command Line Arguments

It is a list of arguments passed to the script from the command line.

```python
import sys

print("Script name:", sys.argv[0])
print("Other arguments:", sys.argv[1:])
```

💡 Run this from command line like:

```
python myscript.py apple banana
```

Output:

```
Script name: myscript.py
Other arguments: ['apple', 'banana']
```

---

## ✅ 3. `sys.exit()` — Exit from Program

It is used to **stop the execution** of the program manually.

```python
import sys

print("Start of program")
sys.exit()
print("This will not print")
```

📌 After `sys.exit()`, the program stops. Nothing below it runs.

---

## ✅ 4. `sys.path` — Module Search Path

Returns a list of paths Python searches when you do `import`.

```python
import sys
for path in sys.path:
    print(path)
```

💡 You can also **add your own folder** to this path to import custom modules.

```python
sys.path.append("/my/custom/folder")
```

---

## ✅ 5. `sys.platform` — Find Operating System

```python
import sys
print(sys.platform)
```

Possible outputs:

* `'win32'` → Windows
* `'linux'` → Linux
* `'darwin'` → macOS

---

## ✅ 6. `sys.stdin`, `sys.stdout`, `sys.stderr` — Streams

These are used for input/output/error handling.

### 🔸 `sys.stdin` → Standard Input

```python
import sys
print("Enter something:")
user_input = sys.stdin.readline()
print("You entered:", user_input)
```

### 🔸 `sys.stdout` → Standard Output

```python
import sys
sys.stdout.write("This is a custom output\n")
```

### 🔸 `sys.stderr` → Standard Error

```python
import sys
sys.stderr.write("This is an error message\n")
```

You won’t usually use these directly unless you’re working with advanced input/output control.

---

## ✅ 7. `sys.getsizeof()` — Memory Size of Objects

```python
import sys

x = 100
print("Size of x in bytes:", sys.getsizeof(x))

s = "hello"
print("Size of string:", sys.getsizeof(s))
```

🧠 Good for checking how much memory your variables are using.

---

## ✅ 8. Other Useful `sys` Functions and Attributes

| Function                   | Use                         |
| -------------------------- | --------------------------- |
| `sys.modules`              | Dict of all loaded modules  |
| `sys.maxsize`              | Max integer value in Python |
| `sys.float_info`           | Info about float precision  |
| `sys.getrecursionlimit()`  | Current recursion limit     |
| `sys.setrecursionlimit(n)` | Set recursion limit         |

Example:

```python
import sys
print("Max recursion limit:", sys.getrecursionlimit())
```

---

## 🧾 Summary Table

| Feature                   | Use                             |
| ------------------------- | ------------------------------- |
| `sys.version`             | Python version info             |
| `sys.argv`                | Command-line arguments          |
| `sys.exit()`              | Manually stop script            |
| `sys.path`                | Import path list                |
| `sys.platform`            | OS info                         |
| `sys.stdin/stdout/stderr` | I/O Streams                     |
| `sys.getsizeof()`         | Size of variable in bytes       |
| `sys.getrecursionlimit()` | Current recursion depth allowed |

---

## 📘 Final Tips

* `sys` is useful when you're working on:

  * CLI (Command Line Interface) tools
  * Custom error messages
  * System-specific behaviors
  * Debugging memory issues