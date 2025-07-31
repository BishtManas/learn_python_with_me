# 🌀 Python `random` Module

The `random` module in Python is used to generate **random numbers** or **randomly select items**. It’s great when you’re building games, simulations, testing tools, or anything that needs some element of randomness.

---

## 🧠 Why use the `random` module?

Because it lets your program do things like:

* Roll a dice
* Shuffle a deck of cards
* Pick a random password
* Randomize quiz questions
* Create unpredictable behavior in games

---

## 🧾 How to Import the `random` Module

```python
import random
```

Once you import it, you can use many functions from the module.

---

## 🧮 Most Common Functions in `random`

### 1. `random.random()`

🔹 Returns a random **float** number between **0.0 and 1.0**

```python
import random
print(random.random())  # e.g., 0.7456
```

---

### 2. `random.uniform(a, b)`

🔹 Returns a random **float** between **a and b**

```python
print(random.uniform(1, 10))  # e.g., 6.378
```

---

### 3. `random.randint(a, b)`

🔹 Returns a random **integer** between **a and b**, both inclusive

```python
print(random.randint(1, 6))  # Like rolling a dice (1 to 6)
```

---

### 4. `random.randrange(start, stop[, step])`

🔹 Works like `range()` but returns a random number from the sequence

```python
print(random.randrange(0, 10, 2))  # Possible: 0, 2, 4, 6, 8
```

---

### 5. `random.choice(sequence)`

🔹 Returns **one random element** from a list, tuple, or string

```python
fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))  # e.g., 'banana'
```

---

### 6. `random.choices(population, k=n)`

🔹 Returns a **list of `k` random elements** (with repetition allowed)

```python
cards = ['♠️', '♥️', '♦️', '♣️']
print(random.choices(cards, k=3))  # e.g., ['♣️', '♥️', '♣️']
```

---

### 7. `random.sample(population, k=n)`

🔹 Returns a **list of `k` unique elements** (no repetition)

```python
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.sample(lottery, k=4))  # e.g., [3, 7, 2, 9]
```

---

### 8. `random.shuffle(sequence)`

🔹 **Shuffles** a list **in-place**

```python
cards = ['A', 'K', 'Q', 'J']
random.shuffle(cards)
print(cards)  # e.g., ['K', 'A', 'J', 'Q']
```

---

### 9. `random.seed(value)`

🔹 Sets the **starting point** for the random number generator (for repeatable results)

```python
random.seed(10)
print(random.random())  # Will always print the same value if the seed is same
```

---

## 💡 Real-Life Mini Examples

### 🎲 Roll a Dice

```python
dice = random.randint(1, 6)
print("You rolled:", dice)
```

---

### 🎯 Pick a Random Student

```python
students = ['Aman', 'Neha', 'Ravi', 'Simran']
print("Selected student:", random.choice(students))
```

---

### 🔀 Shuffle a Playlist

```python
playlist = ['song1', 'song2', 'song3', 'song4']
random.shuffle(playlist)
print("Shuffled playlist:", playlist)
```

---

### 💰 Lottery Number Picker

```python
lottery_numbers = random.sample(range(1, 50), 6)
print("Your lucky numbers:", lottery_numbers)
```

---

## ⚠️ Notes for Beginners

* If you want **random but repeatable behavior**, use `random.seed()`.
* `random.randint()` includes both start and end numbers.
* `random.choices()` allows duplicates, `random.sample()` doesn’t.
* `random.shuffle()` only works with **lists**, not strings or tuples.

---

## 🧪 Practice Ideas for You

* Create a **coin toss simulator** (Heads or Tails).
* Build a **random password generator**.
* Write a **quiz app** that asks questions in random order.
* Make a **number guessing game** using `random.randint()`.

---

## 📦 Summary Table

| Function                       | Purpose                                |
| ------------------------------ | -------------------------------------- |
| `random()`                     | Float from 0.0 to 1.0                  |
| `uniform(a, b)`                | Float between a and b                  |
| `randint(a, b)`                | Integer between a and b (inclusive)    |
| `randrange(start, stop, step)` | Random value like range()              |
| `choice(seq)`                  | One random element from a sequence     |
| `choices(seq, k)`              | Multiple random elements (with repeat) |
| `sample(seq, k)`               | Multiple random elements (no repeat)   |
| `shuffle(list)`                | Randomly rearrange list                |
| `seed(value)`                  | Set the randomness start               |