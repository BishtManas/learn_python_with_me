## TOP PYTHON MODULES USED MOSTLY

---

### 1. **`os`** – Operating System Interface

Used for: working with **files**, **folders**, paths, etc.

```python
import os

print(os.getcwd())  # Get current working directory
os.mkdir("new_folder")  # Create a new folder
```

---

### 2. **`sys`** – System-specific Parameters

Used for: handling **command-line arguments**, exiting the script, etc.

```python
import sys

print(sys.argv)  # List of command-line arguments
sys.exit()       # Exit the program
```

---

### 3. **`math`** – Math Operations

Used for: square roots, trigonometry, constants like pi, etc.

```python
import math

print(math.sqrt(25))   # 5.0
print(math.pi)         # 3.141592...
```

---

### 4. **`random`** – Random Stuff

Used for: games, simulations, data shuffling.

```python
import random

print(random.randint(1, 10))  # Random number from 1 to 10
print(random.choice(['apple', 'banana', 'mango']))
```

---

### 5. **`datetime`** – Dates and Times

Used for: getting current time, date, differences, etc.

```python
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

---

### 6. **`time`** – Time Management

Used for: delays, measuring execution time.

```python
import time

print("Start")
time.sleep(2)  # Wait for 2 seconds
print("End")
```

---

### 7. **`json`** – JSON Data Handling

Used for: APIs, config files, data storage.

```python
import json

data = {"name": "Sir", "age": 22}
json_string = json.dumps(data)  # Convert dict to JSON
print(json_string)
```

---

### 8. **`re`** – Regular Expressions

Used for: pattern matching, email validation, searching strings.

```python
import re

text = "My email is example@gmail.com"
match = re.search(r'\S+@\S+', text)
print(match.group())  # Output: example@gmail.com
```

---

### 9. **`pandas`** – Data Analysis

Used for: handling large datasets, spreadsheets, CSVs.

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```

---

### 10. **`tkinter`** – GUI Applications

Used for: creating simple desktop apps with buttons, labels, etc.

```python
import tkinter as tk

root = tk.Tk()
root.title("My App")
tk.Label(root, text="Hello!").pack()
root.mainloop()
```

---

## ✅ Bonus: Popular 3rd Party Modules (Need to install using `pip`)

| Module       | Used For                    | Install Command          |
| ------------ | --------------------------- | ------------------------ |
| `requests`   | API calls / HTTP requests   | `pip install requests`   |
| `numpy`      | Math, Arrays, ML            | `pip install numpy`      |
| `matplotlib` | Data Visualization / Graphs | `pip install matplotlib` |
| `openpyxl`   | Working with Excel files    | `pip install openpyxl`   |
| `flask`      | Web development             | `pip install flask`      |
