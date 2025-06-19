# 🔥 Python Notes – List, Tuple, Set & Dictionary (Full Guide)

---

## 1️⃣ LIST

### ✅ What is a List?

* An **ordered** collection of **items**
* **Mutable** → you can change it
* **Allows duplicates**
* Can store **mixed data types**

### 🧪 Example:

```python
my_list = [10, 20, "hello", 3.14]
```

### 🔧 Common Operations:

```python
my_list.append(100)       # Add at end
my_list.insert(1, 99)     # Add at index
my_list.remove(20)        # Remove by value
my_list.pop()             # Remove last
my_list.sort()            # Sort (only same data types)
my_list.reverse()         # Reverse
```

### 🔁 Looping:

```python
for item in my_list:
    print(item)
```

---

## 2️⃣ TUPLE

### ✅ What is a Tuple?

* **Ordered**, **immutable** (can’t change)
* **Allows duplicates**
* Faster and safer than list
* Use when data shouldn't change

### 🧪 Example:

```python
my_tuple = (1, 2, 3)
```

### 🧠 Single-item Tuple:

```python
single = (5,)  # Comma is needed
```

### 🔧 Useful Methods:

```python
len(my_tuple)
my_tuple.count(2)
my_tuple.index(3)
```

---

## 3️⃣ SET

### ✅ What is a Set?

* **Unordered**, **mutable**, **no duplicates**
* Best for **unique items**
* Can't access by index

### 🧪 Example:

```python
my_set = {1, 2, 3, 4}
```

### ❗ How to Create an **Empty Set**:

```python
empty_set = set()   # ✅ Correct way
```

> `empty_set = {}` ❌ This creates an **empty dictionary**, not a set.

### 🔧 Common Methods:

```python
my_set.add(5)
my_set.remove(2)
my_set.discard(10)      # No error if item not found
my_set.clear()
```

### 🔁 Set Operations:

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)                  # {1, 2, 3, 4, 5}
a.intersection(b)           # {3}
a.difference(b)             # {1, 2}
a.symmetric_difference(b)   # {1, 2, 4, 5}
```

---

## 4️⃣ DICTIONARY

### ✅ What is a Dictionary?

* **Unordered** collection of **key-value pairs**
* **Mutable**
* Keys must be **unique**
* Values can be anything

### 🧪 Example:

```python
my_dict = {
    "name": "Alice",# "name" is key and "Alice" is value.
    "age": 25,
    "is_student": True
}
```

### 🔧 Accessing Values:

```python
print(my_dict["name"])
print(my_dict.get("age"))
```

### ✏️ Adding / Updating:

```python
my_dict["grade"] = "A"
my_dict["age"] = 26
```

### 🧹 Removing Items:

```python
my_dict.pop("grade")
del my_dict["age"]
my_dict.clear()
```

### 🔁 Looping:

```python
for key, value in my_dict.items():
    print(key, value)
```

### 🧰 Dictionary Methods:

```python
my_dict.keys()
my_dict.values()
my_dict.items()
len(my_dict)
```

---

## 🔍 DIFFERENCE: Empty Set vs Empty Dictionary

| Feature         | `set()`                    | `{}`                       |
| --------------- | -------------------------- | -------------------------- |
| What it creates | An **empty set**           | An **empty dictionary**    |
| Type            | `<class 'set'>`            | `<class 'dict'>`           |
| Example         | `empty_set = set()`        | `empty_dict = {}`          |
| Use case        | Unique collection of items | Key-value pairs            |
| Access by index | ❌ No                       | ❌ No (but access by key ✅) |
| Mutable         | ✅ Yes                      | ✅ Yes                      |

---

## 📚 Quick Summary Table

| Feature           | List  | Tuple | Set            | Dictionary               |
| ----------------- | ----- | ----- | -------------- | ------------------------ |
| Ordered           | ✅ Yes | ✅ Yes | ❌ No           | ❌ (in older) ✅ (in 3.7+) |
| Mutable           | ✅ Yes | ❌ No  | ✅ Yes          | ✅ Yes                    |
| Allows Duplicates | ✅ Yes | ✅ Yes | ❌ No           | ✅ Keys: ❌, Values: ✅     |
| Indexed           | ✅ Yes | ✅ Yes | ❌ No           | ✅ (by key only)          |
| Syntax            | `[]`  | `()`  | `{}` / `set()` | `{key: value}`           |