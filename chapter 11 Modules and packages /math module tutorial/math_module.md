# 🧮 Python `math` Module – Complete Beginner Tutorial

The **`math` module** in Python gives us access to many useful **mathematical functions**, constants (like π), and tools (like square root, power, trigonometry, etc.).

To use the `math` module, you must first **import** it:

```python
import math
```

---

## 📦 1. What is a Module?

A **module** is a file that contains Python code — functions, classes, or variables — that you can use in your own code.

🔸 The `math` module is a **built-in module**, which means Python already provides it, and you just need to import it.

---

## ✅ 2. How to Import `math`

```python
import math
```

Now you can use functions like:

```python
math.sqrt(25)
```

---

## 🧠 3. Common `math` Functions with Simple Examples

| Function            | Meaning                     | Example             | Output     |
| ------------------- | --------------------------- | ------------------- | ---------- |
| `math.sqrt(x)`      | Square root                 | `math.sqrt(16)`     | `4.0`      |
| `math.pow(x, y)`    | x raised to power y         | `math.pow(2, 3)`    | `8.0`      |
| `math.floor(x)`     | Round down to nearest whole | `math.floor(4.7)`   | `4`        |
| `math.ceil(x)`      | Round up to nearest whole   | `math.ceil(4.2)`    | `5`        |
| `math.factorial(x)` | Factorial of x              | `math.factorial(5)` | `120`      |
| `math.fabs(x)`      | Absolute value              | `math.fabs(-7)`     | `7.0`      |
| `math.isqrt(x)`     | Integer square root         | `math.isqrt(10)`    | `3`        |
| `math.log(x)`       | Natural log (base e)        | `math.log(10)`      | `2.302...` |
| `math.log10(x)`     | Log base 10                 | `math.log10(100)`   | `2.0`      |
| `math.gcd(x, y)`    | Greatest common divisor     | `math.gcd(12, 15)`  | `3`        |

---

## ✨ 4. Special Constants in `math`

| Constant  | Description            | Example   |
| --------- | ---------------------- | --------- |
| `math.pi` | π (pi) ≈ 3.14159       | `math.pi` |
| `math.e`  | Euler’s number ≈ 2.718 | `math.e`  |

```python
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
```

---

## 🎯 5. Trigonometry Functions (Basic Overview)

These are used in angles and geometry:

| Function          | Description                  | Example                 | Output    |
| ----------------- | ---------------------------- | ----------------------- | --------- |
| `math.sin(x)`     | Sine of angle x (in radians) | `math.sin(math.pi/2)`   | `1.0`     |
| `math.cos(x)`     | Cosine                       | `math.cos(0)`           | `1.0`     |
| `math.tan(x)`     | Tangent                      | `math.tan(math.pi/4)`   | `~1.0`    |
| `math.radians(x)` | Convert degrees to radians   | `math.radians(180)`     | `3.14159` |
| `math.degrees(x)` | Convert radians to degrees   | `math.degrees(math.pi)` | `180`     |

---

## 💡 6. Example: Area of a Circle

Let’s use `math.pi` and `math.pow()` to calculate the area:

```python
import math

radius = 5
area = math.pi * math.pow(radius, 2)
print("Area of circle:", area)
```

📤 **Output:**

```
Area of circle: 78.53981633974483
```

---

## 🧪 7. Example: Find Square Root of a Number

```python
import math

num = 49
result = math.sqrt(num)
print("Square root:", result)
```

---

## 📌 8. Small Beginner Project Idea Using `math`

### Program to Take User Input and Show Some `math` Results

```python
import math

num = float(input("Enter a number: "))

print("Square root:", math.sqrt(num))
print("Power of 2:", math.pow(num, 2))
print("Floor value:", math.floor(num))
print("Ceil value:", math.ceil(num))
```

---

## 🧠 9. Difference between `math.pow()` and `**` operator

| `math.pow(2, 3)` | returns `8.0` (float)              |
| ---------------- | ---------------------------------- |
| `2 ** 3`         | returns `8` (int) if both are ints |

---

## 📚 10. Summary – What You Learned

✅ What a module is
✅ How to import and use the `math` module
✅ Key functions like `sqrt`, `pow`, `floor`, `ceil`, `log`, `factorial`
✅ Use of `pi`, `e` constants
✅ Some trigonometric and logarithmic functions
✅ Real-world examples using `math`

---

## 🧲 BONUS: Try it Yourself Exercise

Write a Python program that:

* Takes radius from the user
* Calculates area and circumference of a circle
* Uses `math.pi` and `math.pow()`

