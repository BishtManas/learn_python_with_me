# 🕒 Python `time` Module

## 📌 What is the `time` module?

The `time` module in Python lets you **work with time** in your programs. You can:

* Get the current time
* Pause your program
* Measure execution time
* Convert between different time formats

---

## 📚 Topics Covered

1. `time.time()`
2. `time.sleep()`
3. `time.ctime()`
4. `time.localtime()`
5. `time.gmtime()`
6. `time.strftime()`
7. `time.strptime()`
8. `time.mktime()`
9. `time.perf_counter()`
10. `time.process_time()`
11. `time.monotonic()`
12. Real-life use cases

---

## 🔹 1. `time.time()`

### ➤ What it does:

Returns the current time in **seconds** since January 1, 1970 (called Unix Epoch).

```python
import time
print(time.time())  # Example: 1693471984.885728
```

✅ **Use:** Useful for measuring how long a code takes to run.

---

## 🔹 2. `time.sleep()`

### ➤ What it does:

Pauses the program for the number of seconds you give.

```python
import time
print("Start")
time.sleep(3)  # Wait for 3 seconds
print("End")
```

✅ **Use:** Useful when you want to delay something, like animations, retry logic, or waiting for a process.

---

## 🔹 3. `time.ctime()`

### ➤ What it does:

Gives current time in a **readable string format**.

```python
print(time.ctime())  # Output: 'Thu Aug 1 11:45:23 2025'
```

✅ **Use:** Quick and simple way to print human-readable time.

---

## 🔹 4. `time.localtime()`

### ➤ What it does:

Returns the current local time as a `struct_time` object.

```python
local = time.localtime()
print(local)
```

✅ **Use:** To get parts like hour, minute, day, etc.

```python
print("Year:", local.tm_year)
print("Month:", local.tm_mon)
print("Day:", local.tm_mday)
```

---

## 🔹 5. `time.gmtime()`

### ➤ What it does:

Same as `localtime()` but gives time in **UTC** (Coordinated Universal Time).

```python
print(time.gmtime())
```

---

## 🔹 6. `time.strftime(format, time_obj)`

### ➤ What it does:

Formats a `time` object into a **string**.

```python
now = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", now)
print(formatted)  # Output: 2025-08-01 11:46:00
```

🧠 **Common Format Codes:**

| Code | Meaning        | Example |
| ---- | -------------- | ------- |
| %Y   | Year           | 2025    |
| %m   | Month (01-12)  | 08      |
| %d   | Day (01-31)    | 01      |
| %H   | Hour (00-23)   | 11      |
| %M   | Minute (00-59) | 46      |
| %S   | Second (00-59) | 00      |
| %A   | Weekday name   | Friday  |
| %B   | Month name     | August  |

---

## 🔹 7. `time.strptime(string, format)`

### ➤ What it does:

Parses (converts) a **string** into a `struct_time` object.

```python
dt = time.strptime("2025-08-01", "%Y-%m-%d")
print(dt)
```

✅ **Use:** Convert user input or file date into time object.

---

## 🔹 8. `time.mktime(time_obj)`

### ➤ What it does:

Converts a `struct_time` object into **timestamp** (seconds since epoch).

```python
t = time.localtime()
print(time.mktime(t))
```

---

## 🔹 9. `time.perf_counter()`

### ➤ What it does:

High-precision timer (best for performance measuring).

```python
start = time.perf_counter()
for _ in range(1000000): pass
end = time.perf_counter()
print("Time taken:", end - start)
```

✅ **Use:** Best way to measure how fast your code runs.

---

## 🔹 10. `time.process_time()`

### ➤ What it does:

Returns **CPU time** (ignores sleep or wait).

```python
start = time.process_time()
time.sleep(2)
end = time.process_time()
print("CPU Time:", end - start)  # Sleep not counted!
```

---

## 🔹 11. `time.monotonic()`

### ➤ What it does:

Timer that **never goes backward** (good for timers that need stability).

```python
print(time.monotonic())
```

---

## 🧠 Real-Life Use Cases

| Task                      | Best Time Function Used |
| ------------------------- | ----------------------- |
| Delay or wait             | `time.sleep()`          |
| Get readable current time | `time.ctime()`          |
| Get parts of current time | `time.localtime()`      |
| Convert string to time    | `time.strptime()`       |
| Convert time to string    | `time.strftime()`       |
| Measure execution time    | `time.perf_counter()`   |

---

## ✅ Summary Table

| Function         | Description                      |
| ---------------- | -------------------------------- |
| `time()`         | Current timestamp (in seconds)   |
| `sleep()`        | Pause the program                |
| `ctime()`        | Readable current time            |
| `localtime()`    | Local time as object             |
| `gmtime()`       | UTC time as object               |
| `strftime()`     | Format time into string          |
| `strptime()`     | Parse string into time object    |
| `mktime()`       | Convert struct\_time → timestamp |
| `perf_counter()` | Precise code time measurement    |
| `process_time()` | CPU time measurement             |
| `monotonic()`    | Always increasing timer          |