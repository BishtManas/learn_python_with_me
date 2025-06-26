# ⚡ Python List Comprehension – Super Easy Notes

---

## ✅ What is List Comprehension?

List comprehension is a **shorter** and **cleaner** way to create lists using a single line of code.

Instead of writing a `for` loop to build a list, you write it in **one line**.

---

## 🔁 Regular Way vs List Comprehension

### 🔹 Regular Way:

```python
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)
```

🔹 Output:

```
[1, 4, 9, 16, 25]
```

---

### 🔹 With List Comprehension:

```python
squares = [i * i for i in range(1, 6)]
print(squares)
```

✅ Same output, but cleaner and faster to write!

---

## 🧠 Syntax of List Comprehension

```
[expression for item in iterable if condition]
```

| Part         | Meaning                                |
| ------------ | -------------------------------------- |
| `expression` | What to do with each item              |
| `item`       | Temporary variable (like `i`)          |
| `iterable`   | Something you loop over (like `range`) |
| `if` (opt.)  | Optional filter condition              |

---

## 🔥 Examples

---

### ✅ 1. **Simple List Creation**

```python
nums = [i for i in range(5)]
print(nums)
```

🟢 Output:

```
[0, 1, 2, 3, 4]
```

---

### ✅ 2. **Squares of Numbers**

```python
squares = [x * x for x in range(6)]
print(squares)
```

🟢 Output:

```
[0, 1, 4, 9, 16, 25]
```

---

### ✅ 3. **Even Numbers Only**

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

🟢 Output:

```
[0, 2, 4, 6, 8]
```

---

### ✅ 4. **Strings – Uppercase Names**

```python
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)
```

🟢 Output:

```
['ALICE', 'BOB', 'CHARLIE']
```

---

### ✅ 5. **Remove Vowels from a String**

```python
text = "python is powerful"
no_vowels = [ch for ch in text if ch not in "aeiou"]
print("".join(no_vowels))
```

🟢 Output:

```
pythn s pwrfl
```

---

### ✅ 6. **Nested List Comprehension (2D Lists)**

```python
matrix = [[i for i in range(3)] for j in range(3)]
print(matrix)
```

## ⚠️ Things to Avoid

| Mistake                                   | Why it’s wrong               |
| ----------------------------------------- | ---------------------------- |
| Using `print()` inside list comprehension | Not meant for printing stuff |
| Writing too much logic                    | Keep it readable             |
| Nesting too deep                          | Gets hard to read/debug      |

---

## ✅ Summary

* 🔹 Clean, one-line list creation
* 🔹 Use `if` to filter
* 🔹 Use `if-else` for decisions
* 🔹 Makes your code Pythonic 🚀

---

## 🧠 Practice Challenge (Try it now)

1. Create a list of all multiples of 7 from 1 to 100
2. From list `["apple", "banana", "cherry"]`, make all uppercase using list comprehension
3. Create a list of square roots of all even numbers from 1 to 20

---

Want me to make a PDF of this? Or move to the next topic like **OOP** or **Exception Handling practice**?
🟢 Output:

```
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

---

### ✅ 7. **Using `if-else` in List Comprehension**

```python
result = ["even" if i % 2 == 0 else "odd" for i in range(5)]
print(result)
```

🟢 Output:

```
['even', 'odd', 'even', 'odd', 'even']
```

---

## 💡 Bonus: From Regular to Comprehension

### Regular:

```python
new_list = []
for i in range(10):
    if i % 3 == 0:
        new_list.append(i)
```

### Comprehension:

```python
new_list = [i for i in range(10) if i % 3 == 0]
```

Same output: `[0, 3, 6, 9]`

---


