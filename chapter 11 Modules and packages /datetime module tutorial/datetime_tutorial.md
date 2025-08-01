# 🕒 Python `datetime` Module

The `datetime` module in Python helps us **work with dates and times** easily. It lets us:

* Get the current date and time
* Create dates and times manually
* Format dates
* Do date arithmetic (like adding days)
* Find differences between dates

---

## 📦 1. Importing the Module

```python
import datetime
```

You can also import specific classes:

```python
from datetime import date, time, datetime, timedelta
```

---

## 📅 2. `date` Class – Work with Only Date (No Time)

### 👉 Creating a Date

```python
from datetime import date

d = date(2025, 8, 1)   # year, month, day
print(d)  # 2025-08-01
```

### 👉 Get Today's Date

```python
today = date.today()
print(today)  # e.g. 2025-08-01
```

### 👉 Access Year, Month, Day

```python
print(today.year)
print(today.month)
print(today.day)
```

---

## ⏰ 3. `time` Class – Work with Only Time (No Date)

### 👉 Create a Time

```python
from datetime import time

t = time(14, 30, 45)  # hour, minute, second
print(t)  # 14:30:45
```

### 👉 Access Hour, Minute, Second

```python
print(t.hour)
print(t.minute)
print(t.second)
```

---

## 📆 4. `datetime` Class – Work with Both Date and Time

### 👉 Get Current Date & Time

```python
from datetime import datetime

now = datetime.now()
print(now)  # e.g. 2025-08-01 10:15:30.123456
```

### 👉 Create a Specific Date & Time

```python
dt = datetime(2025, 8, 1, 10, 30, 45)
print(dt)
```

### 👉 Access Parts

```python
print(dt.year)
print(dt.month)
print(dt.hour)
print(dt.minute)
```

---

## 🧮 5. `timedelta` – Do Date Math

### 👉 Add or Subtract Days

```python
from datetime import timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)
```

### 👉 Difference Between Two Dates

```python
d1 = date(2025, 8, 10)
d2 = date(2025, 8, 1)

diff = d1 - d2
print(diff.days)  # 9
```

---

## 🛠️ 6. Formatting Dates and Times (`strftime` and `strptime`)

### 👉 `strftime()` – Date to String

```python
now = datetime.now()

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # e.g. 2025-08-01 10:30:00
```

#### Common Format Codes:

| Code | Meaning           | Example |
| ---- | ----------------- | ------- |
| `%Y` | Year (4 digits)   | 2025    |
| `%y` | Year (2 digits)   | 25      |
| `%m` | Month (01 to 12)  | 08      |
| `%d` | Day (01 to 31)    | 01      |
| `%H` | Hour (00 to 23)   | 14      |
| `%M` | Minute (00 to 59) | 45      |
| `%S` | Second (00 to 59) | 30      |
| `%A` | Weekday (name)    | Friday  |
| `%a` | Weekday (short)   | Fri     |

---

### 👉 `strptime()` – String to Date

```python
from datetime import datetime

date_str = "2025-08-01 14:30:00"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt)  # datetime object
```

---

## 🧪 7. Other Useful Features

### 👉 Get Weekday (0=Monday to 6=Sunday)

```python
today = date.today()
print(today.weekday())  # e.g. 4 if it's Friday
```

### 👉 ISO Format

```python
now = datetime.now()
print(now.isoformat())  # e.g. '2025-08-01T10:30:00.123456'
```

---

## ✅ 8. Full Example

```python
from datetime import datetime, timedelta

# Get current date and time
now = datetime.now()

# Add 7 days
next_week = now + timedelta(days=7)

# Format it
formatted = next_week.strftime("Next week date: %A, %d %B %Y")
print(formatted)
```

🟢 Output (Example):

```
Next week date: Friday, 08 August 2025
```

---

## 🧠 Tips for Beginners

* `date` → for dates only (like birthdays)
* `time` → for times only (like setting an alarm)
* `datetime` → when you need both date and time (like event logs)
* `timedelta` → for adding or subtracting time (like 7 days later)
* Use `strftime()` to turn dates into strings.
* Use `strptime()` to turn strings into dates.
