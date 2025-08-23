# **Python Virtual Environment**

## ✅ **What is a Virtual Environment?**

A **virtual environment** is an isolated space in your system where you can install Python packages **independently of the global Python installation**.
This means:

* Different projects can use **different versions of packages**.
* No conflicts between projects.
* Keeps your system clean.

---

## ✅ **Why Do We Need It?**

Imagine you have:

* **Project A** → needs `Django 3.2`
* **Project B** → needs `Django 4.0`

If you install both globally, there will be **version conflicts**.
A virtual environment solves this by **creating a separate environment for each project**.

---

## ✅ **How to Create and Use a Virtual Environment?**

### **Step 1: Check if `venv` is available**

Python 3 comes with `venv` module by default.
Check version:

```bash
python --version
```

---

### **Step 2: Create a Virtual Environment**

Run this command in your project folder:

```bash
python -m venv myenv
```

* `python` → the Python interpreter.
* `-m venv` → tells Python to use the virtual environment module.
* `myenv` → name of the virtual environment folder (you can name it anything).

After this, you will see a **folder named `myenv`** in your project directory.

---

### **Step 3: Activate the Virtual Environment**

* **On Windows:**

```bash
myenv\Scripts\activate
```

* **On macOS / Linux:**

```bash
source myenv/bin/activate
```

✅ **After activation**, you’ll see the environment name in your terminal like:

```
(myenv) $
```

---

### **Step 4: Install Packages Inside Virtual Environment**

Example:

```bash
pip install requests
```

This will install `requests` **only inside `myenv`**, not globally.

---

### **Step 5: Check Installed Packages**

```bash
pip list
```

---

### **Step 6: Deactivate Virtual Environment**

To exit the environment:

```bash
deactivate
```

---

## ✅ **Managing Dependencies**

### **Generate `requirements.txt`**

To save all installed packages:

```bash
pip freeze > requirements.txt
```

### **Install from `requirements.txt`**

If someone else wants the same environment:

```bash
pip install -r requirements.txt
```

---

## ✅ **Good Practices**

✔ Always create a virtual environment for every project.

✔ Never install packages globally unless required.

✔ Commit `requirements.txt` to your project repo.

---

## ✅ **Bonus Tip**

You can also use **`virtualenv`** (older library) or **`conda`** (Anaconda environments) for advanced needs.