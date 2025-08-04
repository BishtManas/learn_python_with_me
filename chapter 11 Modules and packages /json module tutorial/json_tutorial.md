# 🧾 JSON Module in Python

---

## 📌 What is JSON?

**JSON** stands for **JavaScript Object Notation**.

It’s a lightweight data format used to store and exchange data between systems (like web APIs and applications).

> Think of JSON like a dictionary but in string format.

---

## 📦 Why Use `json` Module in Python?

Python provides a built-in module called `json` to:

* Read JSON data ✅
* Write JSON data ✅
* Convert between JSON and Python data ✅

---

## 🔧 How to Import JSON Module

```python
import json
```

---

## 🔄 Python vs JSON Data Types

| Python       | JSON         |
| ------------ | ------------ |
| dict         | object       |
| list, tuple  | array        |
| str          | string       |
| int, float   | number       |
| True / False | true / false |
| None         | null         |

---

## 🔁 Convert Python to JSON

### 👉 Using `json.dumps()`

**`dumps()` = Dump as String**
Converts Python object → JSON string

```python
import json

data = {"name": "Ravi", "age": 25, "is_student": False}

json_str = json.dumps(data)
print(json_str)
```

### 💡 Output:

```json
{"name": "Ravi", "age": 25, "is_student": false}
```

---

## 📝 Save JSON to File

### 👉 Using `json.dump()`

**`dump()` = Dump to File**

```python
import json

data = {"name": "Ravi", "age": 25}

with open("data.json", "w") as file:
    json.dump(data, file)
```

---

## 🔁 Convert JSON to Python

### 👉 Using `json.loads()`

**`loads()` = Load from String**
JSON string → Python object

```python
import json

json_str = '{"name": "Ravi", "age": 25}'

data = json.loads(json_str)
print(data)
```

### 💡 Output:

```python
{'name': 'Ravi', 'age': 25}
```

---

## 📂 Read JSON from File

### 👉 Using `json.load()`

**`load()` = Load from File**

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
```

---

## 🎨 Make JSON Pretty (Readable)

### Use `indent` and `sort_keys`

```python
data = {"name": "Ravi", "age": 25, "country": "India"}

pretty_json = json.dumps(data, indent=4, sort_keys=True)
print(pretty_json)
```

### 💡 Output:

```json
{
    "age": 25,
    "country": "India",
    "name": "Ravi"
}
```

---

## ⚠️ Common Errors

| Error                                                  | Cause                                                                      |
| ------------------------------------------------------ | -------------------------------------------------------------------------- |
| `JSONDecodeError`                                      | JSON string is invalid                                                     |
| `TypeError: Object of type X is not JSON serializable` | You tried to convert an unsupported type (like set, complex, custom class) |

---

## 📌 Custom Encoding (Advanced)

You can convert non-serializable objects (like `datetime`, `set`, custom class) using a custom encoder.

### Example: Encode `set` to `list`

```python
import json

def custom_encoder(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError("Type not serializable")

data = {"fruits": {"apple", "banana"}}

json_str = json.dumps(data, default=custom_encoder)
print(json_str)
```

---

## 🧪 Try it Yourself

### Convert Python dictionary to JSON string:

```python
user = {
    "username": "coder123",
    "skills": ["Python", "AI", "ML"],
    "active": True
}

json_str = json.dumps(user, indent=2)
print(json_str)
```

---

## 📚 Summary

| Method         | Description          |
| -------------- | -------------------- |
| `json.dumps()` | Python → JSON string |
| `json.dump()`  | Python → JSON file   |
| `json.loads()` | JSON string → Python |
| `json.load()`  | JSON file → Python   |

---

## 📁 Bonus Tip: JSON File Format

### Sample `data.json` file

```json
{
  "name": "Ravi",
  "age": 25,
  "skills": ["Python", "Django"],
  "active": true
}
```
