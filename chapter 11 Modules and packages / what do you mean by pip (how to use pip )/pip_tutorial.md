# 🐍 PIP – Beginner Friendly Notes

## 1️⃣ What is PIP?

**PIP** stands for **"Pip Installs Packages"** (or "Preferred Installer Program").
It is the **package manager for Python**.

📌 **In simple words**:
When you need extra tools or libraries in Python (like NumPy, Pandas, Flask), you don’t have to download and set them up manually — **pip** does it for you.

Think of pip as an **app store for Python**.

---

## 2️⃣ Why Do We Need PIP?

Python itself comes with some built-in modules, but for advanced work like:

* Data analysis → `pandas`, `numpy`
* Web development → `flask`, `django`
* AI/ML → `scikit-learn`, `tensorflow`

…you need to **install third-party packages** from the Python Package Index (**PyPI**).
PIP is the tool that fetches and installs them.

---

## 3️⃣ Checking if PIP is Installed

Most Python installations come with pip. To check:

```bash
pip --version
```

Example output:

```
pip 24.0 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)
```

---

## 4️⃣ Installing Packages with PIP

The basic command:

```bash
pip install package_name
```

Example:

```bash
pip install numpy
```

This will:

1. Download NumPy from **PyPI**.
2. Install it so you can use it in Python.

---

## 5️⃣ Installing Specific Versions

Sometimes you need an exact version for compatibility:

```bash
pip install numpy==1.23.5
```

Or a version greater/less than:

```bash
pip install numpy>=1.20
```

---

## 6️⃣ Upgrading a Package

To update a package to the latest version:

```bash
pip install --upgrade numpy
```

---

## 7️⃣ Uninstalling a Package

If you no longer need it:

```bash
pip uninstall numpy
```

---

## 8️⃣ Listing All Installed Packages

```bash
pip list
```

Example:

```
Package    Version
---------- -------
numpy      1.24.3
pandas     2.0.1
```

---

## 9️⃣ Searching for Packages

```bash
pip search package_name
```

*(Note: In some pip versions, search may be disabled — better to use [pypi.org](https://pypi.org) instead.)*

---

## 🔟 Installing from a Requirements File

If you have a file listing packages (usually `requirements.txt`), you can install them all at once:

```bash
pip install -r requirements.txt
```

Example of `requirements.txt`:

```
numpy==1.24.3
pandas==2.0.1
flask>=2.3
```

---

## 1️⃣1️⃣ Installing from a URL or Local File

```bash
pip install https://example.com/package.zip
pip install ./my_package-0.1.tar.gz
```

---

## 1️⃣2️⃣ Extra PIP Commands

| Command                 | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| `pip show package_name` | Info about the package                                           |
| `pip freeze`            | List all packages with exact versions (used in requirements.txt) |
| `pip check`             | Check for broken dependencies                                    |

---

## 1️⃣3️⃣ Best Practices for Using PIP

* Use a **virtual environment** (`venv`) to keep packages for different projects separate.
* Always check package versions for compatibility.
* Keep packages updated to avoid security issues.

---

✅ **Quick Example** – Installing and Using NumPy:

```bash
pip install numpy
```

```python
import numpy as np
print(np.array([1, 2, 3]))
```