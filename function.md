# Python Functions Course

## 📘 Overview
This course provides a complete, structured path to mastering Python functions — from the fundamentals to advanced concepts like decorators, recursion, and generators. It is designed for learners who want practical, real‑world skills and hands‑on exercises.

---

## 🧩 Module 1: Python Functions Basics
### Topics
- What is a function?
- Why functions matter
- Function syntax
- Return values

### Example
```python
def greet():
    print("Hello!")
```

### Exercises
- Create a function that prints your name.
- Create a function that returns the square of a number.

---

## 🧩 Module 2: Python Arguments
### Topics
- Positional arguments
- Keyword arguments
- Default arguments

### Example
```python
def power(base, exp=2):
    return base ** exp
```

### Exercises
- Write a function with default parameters.
- Mix positional and keyword arguments.

---

## 🧩 Module 3: *args and **kwargs
### Topics
- Variable positional arguments (`*args`)
- Variable keyword arguments (`**kwargs`)

### Example
```python
def total(*nums):
    return sum(nums)
```

### Exercises
- Create a function that accepts unlimited numbers and returns the maximum.
- Create a function that prints user profile info using **kwargs.

---

## 🧩 Module 4: Python Scope
### Topics
- Local scope
- Global scope
- The `global` keyword

### Example
```python
x = 10

def show():
    x = 5
    print(x)
```

### Exercises
- Demonstrate local vs global scope.
- Modify a global variable inside a function.

---

## 🧩 Module 5: Python Decorators
### Topics
- What is a decorator?
- How decorators modify behavior
- Writing custom decorators

### Example
```python
def logger(func):
    def wrapper():
        print("Running...")
        func()
    return wrapper

@logger
def greet():
    print("Hello!")
```

### Exercises
- Create a decorator that measures execution time.
- Create a decorator that checks user permissions.

---

## 🧩 Module 6: Python Lambda Functions
### Topics
- Anonymous functions
- Lambdas with `map`, `filter`, `reduce`

### Example
```python
square = lambda x: x * x
```

### Exercises
- Use lambda to sort a list of tuples.
- Use filter + lambda to extract even numbers.

---

## 🧩 Module 7: Python Recursion
### Topics
- What is recursion?
- Base cases
- Recursive patterns

### Example
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
```

### Exercises
- Write a recursive Fibonacci function.
- Write a recursive sum of digits function.

---

## 🧩 Module 8: Python Generators
### Topics
- The `yield` keyword
- Lazy evaluation
- Generator expressions

### Example
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

### Exercises
- Create a generator for even numbers.
- Create a generator that reads a file line by line.

---

## 🧩 Module 9: Code Challenges
### Challenges
- Build a calculator using functions
- Build a student management system using *args/**kwargs
- Build a custom iterator using generators

---

## 🎓 Final Notes
This course equips you with the essential tools to write clean, modular, and efficient Python code. Practice each module thoroughly and complete the challenges to solidify your understanding
# 1. Sum all numbers
Write a function total(*args) that returns the sum of all passed numbers.
total(1, 2, 3)     → 6
total(10, 20)      → 30

## Multiply all
Write a function multiply(*args) that returns the product of all numbers.
multiply(2, 3, 4)  → 24
## About iterator
Create a tuple called mytuple with the values "apple", "banana", "cherry"

Create a variable myit and use iter() on the tuple

Print the first item using next()


### correction 
You are working on a data‑analytics script for a company that processes thousands of sensor readings from different devices. Each device may send data in different formats, and the processing steps may vary depending on the device type.
You need to build a flexible processing system that:
• 	Accepts any number of processing functions using 
• 	Accepts optional configuration settings using 
• 	Uses an iterator to process the sensor readings one at a time, instead of loading everything into memory

❓ The Question
Write a Python function called  that:
1. 	Accepts a list of sensor readings.
2. 	Accepts any number of processing functions using .
3. 	Accepts optional configuration settings using  (e.g., , ).
4. 	Returns an iterator that yields processed readings one by one.
5. 	Applies each processing function to every reading in order.
6. 	If , stop iteration and raise an exception when a processing function fails.
7. 	If , skip the faulty reading and continue.