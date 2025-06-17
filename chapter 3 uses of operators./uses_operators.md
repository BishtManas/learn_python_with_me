## 🧠 Python Operators - Full Concept Notes (With Examples)

In Python, **operators** are used to perform actions on variables and values — like adding numbers, comparing values, assigning data, and more.

There are **7 main types of operators** in Python:

---

### 1️⃣ Arithmetic Operators

These are used to do basic **math operations**:

| Operator | Meaning             | Example (`a = 10`, `b = 3`) | Result |
| -------- | ------------------- | --------------------------- | ------ |
| `+`      | Addition            | `a + b`                     | `13`   |
| `-`      | Subtraction         | `a - b`                     | `7`    |
| `*`      | Multiplication      | `a * b`                     | `30`   |
| `/`      | Division            | `a / b`                     | `3.33` |
| `//`     | Floor Division      | `a // b`                    | `3`    |
| `%`      | Modulus (remainder) | `a % b`                     | `1`    |
| `**`     | Exponent (power)    | `a ** b`                    | `1000` |

🟢 **Where used?**
Calculators, game scores, interest calculators, and more.

---

### 2️⃣ Assignment Operators

Used to **assign or update** values in variables.

| Operator | Meaning             | Example   | Same As      |
| -------- | ------------------- | --------- | ------------ |
| `=`      | Assign value        | `x = 5`   | -            |
| `+=`     | Add and assign      | `x += 2`  | `x = x + 2`  |
| `-=`     | Subtract and assign | `x -= 1`  | `x = x - 1`  |
| `*=`     | Multiply and assign | `x *= 3`  | `x = x * 3`  |
| `/=`     | Divide and assign   | `x /= 2`  | `x = x / 2`  |
| `//=`    | Floor divide assign | `x //= 2` | `x = x // 2` |
| `%=`     | Modulus and assign  | `x %= 2`  | `x = x % 2`  |
| `**=`    | Exponent and assign | `x **= 3` | `x = x ** 3` |

🟢 **Where used?**
To keep updating a score, count, or value in loops or games.

---

### 3️⃣ Comparison Operators

These compare two values and return **True or False**.

| Operator | Meaning          | Example  | Result |
| -------- | ---------------- | -------- | ------ |
| `==`     | Equal to         | `a == b` | False  |
| `!=`     | Not equal to     | `a != b` | True   |
| `>`      | Greater than     | `a > b`  | True   |
| `<`      | Less than        | `a < b`  | False  |
| `>=`     | Greater or equal | `a >= b` | True   |
| `<=`     | Less or equal    | `a <= b` | False  |

🟢 **Where used?**
Used in `if` conditions, filters, and decision-making.

---

### 4️⃣ Logical Operators

Used to combine multiple **conditions**.

| Operator | Meaning               | Example            | Result |
| -------- | --------------------- | ------------------ | ------ |
| `and`    | True if both are True | `x > 5 and x < 10` | True   |
| `or`     | True if one is True   | `x > 5 or x < 2`   | True   |
| `not`    | Opposite result       | `not(x > 5)`       | False  |

🟢 **Where used?**
Used in `if-else` logic, validation checks, search filters, etc.

---

### 5️⃣ Identity Operators

They check whether two variables point to the **same object in memory**.

| Operator | Meaning           | Example      | Result       |
| -------- | ----------------- | ------------ | ------------ |
| `is`     | Same object       | `a is b`     | True / False |
| `is not` | Different objects | `a is not b` | True / False |

🟢 **Where used?**
Used for memory checks, caching, and optimization.

---

### 6️⃣ Membership Operators

They check whether a **value exists** in a sequence like a list, string, or tuple.

| Operator | Meaning             | Example            | Result |
| -------- | ------------------- | ------------------ | ------ |
| `in`     | Value exists        | `5 in [1,2,5]`     | True   |
| `not in` | Value doesn’t exist | `3 not in [1,2,5]` | True   |

🟢 **Where used?**
Used in search, filters, form validations, etc.

---

### 7️⃣ Bitwise Operators (Advanced)

These work on numbers in **binary form**.

| Operator | Name        | Description                         |                               |
| -------- | ----------- | ----------------------------------- | ----------------------------- |
| `&`      | AND         | Only 1 if both bits are 1           |                               |
| \`       | \`          | OR                                  | 1 if any one of the bits is 1 |
| `^`      | XOR         | 1 if bits are different             |                               |
| `~`      | NOT         | Inverts the bits (0→1, 1→0)         |                               |
| `<<`     | Left Shift  | Shifts bits to left (multiply by 2) |                               |
| `>>`     | Right Shift | Shifts bits to right (divide by 2)  |                               |

🟡 **Where used?**
Used in low-level programming, hardware, image processing, encryption.

---

### 🔥 Summary

| Type       | Real Life Use Examples                            |
| ---------- | ------------------------------------------------- |
| Arithmetic | Calculations, scores, price, speed, etc.          |
| Assignment | Updating values, counters, loops                  |
| Comparison | Conditions, access control, logic building        |
| Logical    | Validating multiple conditions, `if` decisions    |
| Identity   | Memory management, object comparison              |
| Membership | Search inside lists, strings, user input checks   |
| Bitwise    | Binary data, encryption, games, performance tasks |