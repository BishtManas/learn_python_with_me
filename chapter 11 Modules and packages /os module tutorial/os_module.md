# 🧠 Python `os` Module

The `os` module in Python allows you to interact with the **Operating System**. It helps you:

* Work with files and folders
* Get system information
* Run terminal/command line commands
* Handle environment variables

Let’s go step-by-step and cover all the important parts!

---

## ✅ 1. Importing the Module

```python
import os
```

---

## 📁 2. Working with Directories (Folders)

### 🔍 `os.getcwd()` – Get Current Working Directory

```python
print(os.getcwd())
```

> 💡 Shows the folder where your script is running.

---

### 📂 `os.chdir(path)` – Change Directory

```python
os.chdir("C:/Users/YourName/Documents")
```

> ✅ Changes the current working directory to a new location.

---

### 📁 `os.listdir(path='.')` – List Files and Folders

```python
print(os.listdir())  # current directory
print(os.listdir("C:/Users"))  # specific path
```

> 📃 Returns a list of file and folder names in the path.

---

### 🧱 `os.mkdir(name)` – Create New Folder

```python
os.mkdir("new_folder")
```

> 📁 Creates a new folder (only one level).

---

### 🧱 `os.makedirs(name)` – Create Folders (Including Parents)

```python
os.makedirs("folder1/folder2/folder3")
```

> 📂 Creates nested folders all at once.

---

### ❌ `os.remove(path)` – Delete a File

```python
os.remove("myfile.txt")
```

> ⚠️ Only works on files, not folders.

---

### ❌ `os.rmdir(path)` – Remove Empty Folder

```python
os.rmdir("empty_folder")
```

> ⚠️ Folder must be empty.

---

### ❌ `os.removedirs(path)` – Remove Directory Tree

```python
os.removedirs("folder1/folder2/folder3")
```

> 🪓 Removes folders and parent folders (if empty).

---

## 🔁 3. File and Directory Operations

### 🏷️ `os.rename(src, dst)` – Rename a File or Folder

```python
os.rename("old_name.txt", "new_name.txt")
```

> 📝 Works for both files and folders.

---

### 📊 `os.stat(path)` – Get File Info

```python
info = os.stat("myfile.txt")
print(info.st_size)  # file size
```

> 📈 Returns file metadata like size, modified time, etc.

---

### 🔎 `os.path.exists(path)` – Check if File/Folder Exists

```python
print(os.path.exists("notes.txt"))
```

> ✅ Returns `True` or `False`.

---

### 📁 `os.path.isdir(path)` – Check if it’s a Directory

```python
os.path.isdir("my_folder")
```

---

### 📄 `os.path.isfile(path)` – Check if it’s a File

```python
os.path.isfile("myfile.txt")
```

---

## 🧾 4. Path Handling (`os.path` submodule)

### 🧩 `os.path.join(a, b)` – Join Paths Correctly

```python
folder = "C:/Users/YourName"
file = "notes.txt"
print(os.path.join(folder, file))
```

> 🧠 It handles different OS formats (like `/` vs `\`).

---

### 📂 `os.path.basename(path)` – Get File Name Only

```python
os.path.basename("C:/Users/YourName/file.txt")
# Output: file.txt
```

---

### 📁 `os.path.dirname(path)` – Get Folder Path Only

```python
os.path.dirname("C:/Users/YourName/file.txt")
# Output: C:/Users/YourName
```

---

### 🔄 `os.path.split(path)` – Split Path into Folder and File

```python
os.path.split("C:/Users/YourName/file.txt")
# Output: ('C:/Users/YourName', 'file.txt')
```

---

### 📦 `os.path.splitext(path)` – Split File and Extension

```python
os.path.splitext("notes.txt")
# Output: ('notes', '.txt')
```

---

## 💻 5. Running OS Commands

### 🧨 `os.system("command")` – Run Terminal/Command Prompt Commands

```python
os.system("dir")  # Windows
os.system("ls")   # Linux/macOS
```

> ⚠️ Be careful – it's like typing directly in your system's terminal!

---

## 🌿 6. Environment Variables

### 🌍 `os.environ` – Access Environment Variables

```python
print(os.environ["PATH"])
```

> 🧠 These are system-level variables like `PATH`, `USERNAME`, etc.

---

### ➕ `os.environ.get("VARIABLE")` – Safe Way to Get Value

```python
username = os.environ.get("USERNAME")
print(username)
```

> ❌ Doesn’t crash if the variable doesn’t exist.

---

## 🧪 7. Useful Examples

### Example: List All `.txt` Files in a Folder

```python
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)
```

---

### Example: Create Folder if Not Exists

```python
if not os.path.exists("my_data"):
    os.mkdir("my_data")
```

---

## 🛑 Be Careful With:

* `os.remove()` – deletes files permanently.
* `os.rmdir()` – only works if the folder is empty.
* `os.system()` – don’t run harmful commands by mistake!

---

## 📌 Summary Cheat Sheet

| Function                      | Use                         |
| ----------------------------- | --------------------------- |
| `os.getcwd()`                 | Get current directory       |
| `os.chdir()`                  | Change directory            |
| `os.listdir()`                | List files/folders          |
| `os.mkdir()` / `makedirs()`   | Create folder(s)            |
| `os.remove()`                 | Delete file                 |
| `os.rmdir()` / `removedirs()` | Delete folder(s)            |
| `os.rename()`                 | Rename file/folder          |
| `os.path.exists()`            | Check if path exists        |
| `os.path.join()`              | Combine paths               |
| `os.environ.get()`            | Access environment variable |

---

## 🚀 Tip for Practice

Try building a small Python script to:

* Organize files into folders by type (`.txt`, `.jpg`, etc.)
* Rename multiple files in a folder
* Create backup folders automatically