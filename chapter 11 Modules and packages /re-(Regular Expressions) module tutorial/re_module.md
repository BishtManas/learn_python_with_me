# 🐍 Python `re` Module

The `re` module in Python is used for **working with Regular Expressions** (regex).
A **regular expression** is a sequence of characters that forms a **search pattern**, often used for searching, matching, or manipulating strings.

---

## 📌 1. Importing the `re` Module

Before using regex, import the `re` module:

```python
import re
```

---

## 📌 2. Common Functions in `re` Module

| Function                        | Description                                             | Returns                |
| ------------------------------- | ------------------------------------------------------- | ---------------------- |
| `re.match(pattern, string)`     | Matches the pattern **only at the start** of the string | Match object or `None` |
| `re.search(pattern, string)`    | Searches **anywhere** in the string for the first match | Match object or `None` |
| `re.findall(pattern, string)`   | Returns **all matches** as a list                       | List of strings        |
| `re.finditer(pattern, string)`  | Returns **iterator** of match objects                   | Iterator               |
| `re.sub(pattern, repl, string)` | Replaces matches with another string                    | New string             |
| `re.split(pattern, string)`     | Splits string at matches                                | List of strings        |
| `re.fullmatch(pattern, string)` | Checks if the **whole string** matches the pattern      | Match object or `None` |
| `re.compile(pattern)`           | Compiles a regex pattern for reuse                      | Pattern object         |

---

## 📌 3. Match Object Methods

When you get a match object (from `match`, `search`, or `finditer`), you can use:

| Method     | Description                 |
| ---------- | --------------------------- |
| `.group()` | Returns the matched string  |
| `.start()` | Starting index of the match |
| `.end()`   | Ending index of the match   |
| `.span()`  | Tuple of (start, end)       |

Example:

```python
import re
text = "Hello World"
match = re.search(r"World", text)

if match:
    print(match.group())   # World
    print(match.start())   # 6
    print(match.end())     # 11
    print(match.span())    # (6, 11)
```

---

## 📌 4. Basic Pattern Syntax

### **Literals**

* `abc` → matches exactly `abc`

### **Meta-characters** (Special Characters in regex)

These characters have special meanings:

| Symbol  | Meaning                                  |
| ------- | ---------------------------------------- |
| `.`     | Any character except newline             |
| `^`     | Start of string                          |
| `$`     | End of string                            |
| `*`     | 0 or more repetitions                    |
| `+`     | 1 or more repetitions                    |
| `?`     | 0 or 1 repetition                        |
| `{n}`   | Exactly n repetitions                    |
| `{n,}`  | n or more repetitions                    |
| `{n,m}` | Between n and m repetitions              |
| `[]`    | Matches any one character from set       |
| `[^ ]`  | Matches any one character **not** in set |
| `\`     | Escapes special characters               |
| `\|`    | OR operator                              |

---

## 📌 5. Predefined Character Classes

| Pattern | Matches                              |
| ------- | ------------------------------------ |
| `\d`    | Digit (0–9)                          |
| `\D`    | Not a digit                          |
| `\w`    | Word character (letters, digits, \_) |
| `\W`    | Not a word character                 |
| `\s`    | Whitespace (space, tab, newline)     |
| `\S`    | Not whitespace                       |

---

## 📌 6. Grouping & Capturing

### **Using parentheses `( )`**

* `(abc)` → group
* Access with `.group(1)`, `.group(2)`, etc.

Example:

```python
text = "Name: John Age: 25"
match = re.search(r"Name: (\w+) Age: (\d+)", text)
print(match.group(1))  # John
print(match.group(2))  # 25
```

---

## 📌 7. Alternation (OR)

* Use `|` to match one of many patterns:

```python
re.search(r"cat|dog", "I have a dog")  # Matches 'dog'
```

---

## 📌 8. Anchors – Start & End of String

| Pattern    | Matches            |
| ---------- | ------------------ |
| `^pattern` | Match at the start |
| `pattern$` | Match at the end   |

Example:

```python
re.match(r"Hello", "Hello World")  # ✅
re.match(r"World", "Hello World")  # ❌
```

---

## 📌 9. Quantifiers

| Pattern  | Meaning             |
| -------- | ------------------- |
| `a*`     | 0 or more a's       |
| `a+`     | 1 or more a's       |
| `a?`     | 0 or 1 a            |
| `a{3}`   | Exactly 3 a's       |
| `a{2,4}` | Between 2 and 4 a's |

---

## 📌 10. Lookahead & Lookbehind

### **Lookahead**

* `X(?=Y)` → X only if followed by Y
* `X(?!Y)` → X only if NOT followed by Y

### **Lookbehind**

* `(?<=Y)X` → X only if preceded by Y
* `(?<!Y)X` → X only if NOT preceded by Y

Example:

```python
re.search(r"\d+(?= dollars)", "100 dollars")  # '100'
re.search(r"(?<=USD )\d+", "USD 100")  # '100'
```

---

## 📌 11. Flags in `re` Module

| Flag                      | Meaning                                    |
| ------------------------- | ------------------------------------------ |
| `re.IGNORECASE` or `re.I` | Case-insensitive match                     |
| `re.MULTILINE` or `re.M`  | `^` and `$` match at each line’s start/end |
| `re.DOTALL` or `re.S`     | `.` matches newline too                    |
| `re.VERBOSE` or `re.X`    | Allows comments and multi-line regex       |

Example:

```python
re.search(r"hello", "HELLO", re.I)  # ✅ Match
```

---

## 📌 12. `re.sub()` – Replace Strings

```python
text = "apple banana apple"
new_text = re.sub(r"apple", "orange", text)
print(new_text)  # orange banana orange
```

---

## 📌 13. `re.split()` – Split by Regex

```python
text = "one, two; three"
parts = re.split(r"[,;]\s*", text)
print(parts)  # ['one', 'two', 'three']
```

---

## 📌 14. Compiling Patterns for Reuse

```python
pattern = re.compile(r"\d+")
print(pattern.findall("123 abc 456"))  # ['123', '456']
```

---

## 📌 15. Escaping Special Characters

Use `\` or `re.escape()`:

```python
print(re.escape("Hello. How are you?"))
# Output: Hello\. How\ are\ you\?
```

---

## 📌 16. Real-Life Examples

✅ **Extract Emails**

```python
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", 
                    "Contact: test@example.com, info@mail.com")
print(emails)  # ['test@example.com', 'info@mail.com']
```

✅ **Validate Phone Number**

```python
pattern = r"^\+91\d{10}$"
print(bool(re.match(pattern, "+911234567890")))  # True
```

✅ **Find All Hashtags**

```python
text = "Love #python and #coding"
hashtags = re.findall(r"#\w+", text)
print(hashtags)  # ['#python', '#coding']
```

---

## 📌 17. Summary Table

| Feature              | Function/Pattern         |
| -------------------- | ------------------------ |
| Search from start    | `re.match()`             |
| Search anywhere      | `re.search()`            |
| All matches list     | `re.findall()`           |
| All matches iterator | `re.finditer()`          |
| Replace text         | `re.sub()`               |
| Split text           | `re.split()`             |
| Compile regex        | `re.compile()`           |
| Flags                | `re.I, re.M, re.S, re.X` |