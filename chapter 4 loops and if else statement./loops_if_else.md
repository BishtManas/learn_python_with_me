1. ✅ What is `if-else`
2. ✅ How it works (with code)
3. ✅ What are `loops` (`for`, `while`)
4. ✅ Real examples
5. ✅ Best practices
6. ✅ Comments everywhere so you can copy to VS Code and run it directly.

---

## 🧠 1. IF-ELSE STATEMENTS IN PYTHON

### 🟢 What is it?

It’s used to make **decisions**. Like:

> “If I have money, I’ll buy pizza. Else, I’ll make Maggi.”

### 🧱 Structure:

```python
if condition:
    # do this if condition is True
elif another_condition:
    # do this if the above was False but this is True
else:
    # do this if none of the above conditions are True
```

---

### 🔁 Example:

```python
age = 18

if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ Sorry, you are not eligible.")
```

### 👇 Another Example with `elif`:

```python
marks = 75

if marks >= 90:
    print("🎉 Grade A")
elif marks >= 70:
    print("🙂 Grade B")
elif marks >= 50:
    print("😐 Grade C")
else:
    print("❌ Failed")
```

---

## 🔁 2. LOOPS IN PYTHON

### 💬 Why Loops?

Loops help you to **repeat** something without writing it again and again.

Like:

> “Say Hello 10 times”
> You use a loop instead of writing 10 print lines.

---

### 🔄 Types of Loops:

1. `for` loop – Runs a block **for a known number of times**
2. `while` loop – Runs **until a condition becomes false**

---

### ✅ FOR LOOP

```python
# Print numbers from 1 to 5
for i in range(1, 6):
    print("Number:", i)
```

> `range(1,6)` means: 1, 2, 3, 4, 5 (6 is excluded)

---

### ✅ WHILE LOOP

```python
# Print numbers from 1 to 5 using while loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1  # Increase by 1
```

---

## 🚨 Infinite Loop (Be Careful!)

```python
# This will run forever if you forget to increase the count
while True:
    print("This will never stop")
```

---

## 🔥 More Examples

### ✅ Print even numbers from 1 to 10

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
```

---

### ✅ Check if number is positive, negative, or zero

```python
num = int(input("Enter a number: "))

if num > 0:
    print("It's a positive number.")
elif num < 0:
    print("It's a negative number.")
else:
    print("It's zero.")
```

---

### ✅ Nested if-else (inside another if)

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You can vote.")
    else:
        print("You are not a citizen, can't vote.")
else:
    print("You are too young to vote.")
```

---

## 🧠 Best Practices

✅ Use proper **indentation** (4 spaces or 1 tab)
✅ Always write meaningful variable names
✅ Be careful of **infinite loops**
✅ Keep `else` at the end

---

## 🎯 Summary

| Concept      | Use                                |
| ------------ | ---------------------------------- |
| `if-else`    | Making decisions                   |
| `for` loop   | Repeat for a known number of times |
| `while` loop | Repeat while condition is true     |
