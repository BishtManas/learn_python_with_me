# 📁 Python File Handling – Full Notes (Text + CSV Files)

---

## ✅ What is File Handling?

File handling means working with files — like creating a file, opening it, reading from it, writing to it, updating it, or deleting it — using Python code.

Just like you use Notepad to write and read `.txt` files, Python can do that too, using code.

---

## 🧰 Built-in Python Functions for File Handling

```python
open()      # To open a file
read()      # To read the file
write()     # To write to the file
close()     # To close the file
readline()  # To read one line at a time
readlines() # To read all lines into a list
```

---

## 🔓 Opening a File

Syntax:

```python
file = open("filename.txt", "mode")
```

### 📌 Modes in File Handling

| Mode  | Meaning                                                  |
| ----- | -------------------------------------------------------- |
| `'r'` | Read mode (default)                                      |
| `'w'` | Write mode (overwrites existing file or creates new)     |
| `'a'` | Append mode (adds content to end)                        |
| `'x'` | Create mode (creates a file, gives error if file exists) |
| `'b'` | Binary mode (for images, PDFs etc)                       |
| `'t'` | Text mode (default)                                      |

👉 Example:

```python
file = open("data.txt", "r")  # open for reading
```

---

## 📖 Reading from a `.txt` File

```python
file = open("data.txt", "r")

print(file.read())      # Reads the entire content
print(file.readline())  # Reads one line
print(file.readlines()) # Returns all lines as list

file.close()
```

---

## ✍️ Writing to a `.txt` File

```python
file = open("data.txt", "w")  # This clears old content
file.write("Hello, Python!\n")
file.write("Learning file handling.")
file.close()
```

> 🔥 Tip: `'w'` mode **overwrites** the file every time.

---

## ➕ Append Mode (`'a'`) – Add without removing old content

```python
file = open("data.txt", "a")
file.write("\nThis line is added later.")
file.close()
```

---

## 🚀 Best Practice: Using `with` keyword (Auto closes file)

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# No need for file.close()
```

---

# 📑 CSV File Handling in Python

CSV = Comma Separated Values
It’s like a table stored in a file, where each row is a line and columns are separated by commas.

**Example CSV:**

```
Name,Age,City
John,23,Delhi
Tina,30,Mumbai
```

---

## 🧪 Reading a CSV File

We use Python’s `csv` module.

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

> Output: Each row is printed as a list
> `['Name', 'Age', 'City']`
> `['John', '23', 'Delhi']`

---

## 📝 Writing to a CSV File

```python
import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 25, "Delhi"])
    writer.writerow(["Sara", 29, "Mumbai"])
```

---

## ➕ Appending to a CSV File

```python
import csv

with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Ravi", 34, "Chennai"])
```

---

## 📚 CSV as Dictionary – `DictReader` and `DictWriter`

### Read CSV into Dictionary

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])
```

### Write CSV from Dictionary

```python
import csv

with open('data.csv', 'w', newline='') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"Name": "John", "Age": 23, "City": "Pune"})
    writer.writerow({"Name": "Amit", "Age": 31, "City": "Kolkata"})
```

---

## 🧹 Extra Stuff You Should Know

### 🔍 Check if file exists

```python
import os

if os.path.exists("file.txt"):
    print("Yes! File exists.")
else:
    print("Nope! File does not exist.")
```

### 🗑️ Delete a File

```python
import os

os.remove("file.txt")
```

---

## ✅ Summary (Key Takeaways)

* Use `open()` with proper mode: `'r'`, `'w'`, `'a'`
* Always `close()` file or use `with open()`
* For `.txt`: use `read()`, `write()`, etc.
* For `.csv`: use `csv.reader()` and `csv.writer()`
* Use `os` module to check or delete files
* Use `newline=''` in CSV to avoid blank lines
