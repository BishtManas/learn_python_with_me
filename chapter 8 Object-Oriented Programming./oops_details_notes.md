# 🧠 Python OOPs (Object-Oriented Programming).
---

## 📌 What is OOP?

OOP (Object-Oriented Programming) is a way of writing code that organizes data and actions (functions) into **objects**.

Think of **objects** like real-world things — for example, a **car** has properties like color, brand, speed (called *attributes*) and it can perform actions like drive, brake (called *methods*).

---

## ⚙️ OOP Concepts in Python

Python supports 4 main OOP concepts:

| No. | Concept       | Meaning (Simple Words)                     |
| --- | ------------- | ------------------------------------------ |
| 1.  | Class         | A blueprint (template) to create objects   |
| 2.  | Object        | A real instance (created from class)       |
| 3.  | Inheritance   | One class can use another class’s features |
| 4.  | Polymorphism  | One thing behaves in different ways        |
| 5.  | Encapsulation | Hiding internal details from outside       |
| 6.  | Abstraction   | Showing only important stuff, hiding rest  |

---

## 🧱 1. Class and Object

### ✅ Class

A **class** is like a template. It defines what data and behavior the objects will have.

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")
```

### ✅ Object

An **object** is created from a class. It’s the actual thing you use.

```python
s1 = Student("Rahul", 20)
s1.greet()  # Output: Hello, my name is Rahul
```

---

## 🧠 What is `__init__`?

* It's a **constructor**.
* Automatically runs when object is created.
* Used to set initial values.

---

## 🔐 2. Encapsulation

Encapsulation means **hiding the internal details** and protecting data from outside interference.

We use **private variables** (by using underscore `_` or `__`) to do this.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
```

> You can’t directly access `__balance` from outside. That’s encapsulation.

---

## 🧬 3. Inheritance

Inheritance means one class can **inherit** features from another class.

### ✅ Example:

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):  # Dog inherits Animal
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()  # Output: Dog barks
```

✅ Benefits:

* Code reuse
* Makes code organized

---

## 🔁 4. Polymorphism

Polymorphism means **many forms** — same function name can behave differently depending on object.

```python
class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

def animal_sound(animal):
    animal.sound()

c1 = Cat()
c2 = Cow()

animal_sound(c1)  # Meow
animal_sound(c2)  # Moo
```

---

## 🎭 5. Abstraction

Abstraction means **hiding unnecessary details** and showing only essentials.

We use **abstract classes** for this using `abc` module.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()  # Output: Car started
```

> You can’t create object of abstract class. You must implement abstract methods in child class.

---

## 👷‍♂️ Extra OOP Features in Python

### 🔹 `self`

* Refers to the current object.
* Always used inside class methods.

```python
def show(self):
    print(self.name)
```

---

### 🔹 `super()`

* Used to call parent class methods.

```python
class Parent:
    def greet(self):
        print("Hello from parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from child")

c = Child()
c.greet()
```

---

## 📦 Types of Methods in Class

| Type            | Description                               |
| --------------- | ----------------------------------------- |
| Instance Method | Works on object (has `self`)              |
| Class Method    | Works on class level (has `cls`)          |
| Static Method   | No `self`, independent logic inside class |

```python
class Demo:
    @staticmethod
    def hello():
        print("Hello")

    @classmethod
    def info(cls):
        print("Class method")

    def greet(self):
        print("Instance method")

d = Demo()
d.greet()
Demo.hello()
Demo.info()
```

---

## 💬 Summary (OOP in Short)

| OOP Concept   | Real-Life Example                         |
| ------------- | ----------------------------------------- |
| Class         | Blueprint of Car                          |
| Object        | Real Car created from that blueprint      |
| Encapsulation | Car engine hidden inside body             |
| Inheritance   | SportsCar inherits Car features           |
| Polymorphism  | Brake works differently in different cars |
| Abstraction   | Driver sees only steering, not wiring     |

---

## ✅ Practice Ideas

* Create a `Book` class with title, author, price
* Create a `Calculator` class (add, subtract, multiply)
* Make a `Shape` base class → `Circle` and `Rectangle` inherit and override `area()`