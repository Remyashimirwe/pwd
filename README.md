# 🐍 Python Lesson: Operators & Conditional Statements

Welcome to today’s Python lesson!
In this chapter, we learn how Python makes decisions using **operators** and **conditional statements**.

These topics are used in real-world programs such as:

- Login systems
- ATM withdrawals
- Shopping discounts
- Student grading
- Weather alerts

---

## 📌 PART 1: Python Operators

Operators are symbols that allow Python to perform actions like comparing values, combining conditions, or updating variables.

---

### ✅ 1. Comparison Operators

Comparison operators compare two values and return `True` or `False`.

| Operator | Meaning | Example |
|---------|---------|---------|
| `==` | Equal to | `x == 10` |
| `!=` | Not equal | `x != 5` |
| `>`  | Greater than | `age > 18` |
| `<`  | Less than | `temp < 20` |
| `>=` | Greater or equal | `marks >= 50` |
| `<=` | Less or equal | `time <= 10` |

Example:

```python
age = 20
print(age > 18)  # True
```

### ✅ 2. Logical Operators

Logical operators combine multiple conditions.

Operator — Meaning
- `and` — Both conditions must be true
- `or` — At least one condition must be true
- `not` — Reverses the condition

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter.")
```

### ✅ 3. Assignment Operators

Assignment operators update values easily.

Operator — Example — Meaning
- `=` — Assign value — `x = 10`
- `+=` — Add and assign — `x += 5`
- `-=` — Subtract and assign — `x -= 2`
- `*=` — Multiply and assign — `x *= 3`
`/=` — Divide and assign — `x /= 2`

Example:

```python
balance = 1000
balance += 500
print(balance)  # 1500
```

### ✅ 4. Membership & Identity Operators

Membership Operators — Used to check if something exists inside a list or string.

- `in` — Found inside
- `not in` — Not found

Example:

```python
fruits = ["apple", "banana"]
print("banana" in fruits)  # True
```

Identity Operators — Used to check if two variables are the same object.

- `is` — Same object
- `is not` — Different object

Example:

```python
x = 10
y = 10
print(x is y)
```

---

🔀 PART 2: Conditional Statements

Conditional statements allow Python programs to make decisions.

### ✅ 1. if Statement

Runs only when the condition is true.

```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")
```

### ✅ 2. if–else Statement

Provides two possible outcomes.

```python
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You are too young.")
```

### ✅ 3. if–elif–else Statement

Used for multiple conditions.

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
else:
    print("Grade: C or below")
```

---

📝 Real-World Practice Questions

Solve these problems using operators and conditional statements:

1. Login Password Check

   Write a program that asks the user for a password. If it matches "admin123", print "Access Granted", otherwise print "Access Denied".

2. Shopping Discount

   A customer gets a discount if they spend more than $100. Check if they qualify.

3. Exam Pass or Fail

   Input marks. If marks are 50 or more, print "Pass", otherwise "Fail".

4. Club Entry Rule

   A person can enter only if they are 18+ AND have an ID card.

5. Extreme Weather Alert

   If temperature is below 0 OR above 35, print "Extreme Weather Warning".

6. Traffic Light System

   If light is:

   - "red" → Stop
   - "yellow" → Get Ready
   - "green" → Go

7. Bank Withdrawal

   If balance is enough, allow withdrawal. Otherwise print "Insufficient funds".

8. Student Grading System

   Input a score and print:

   - A (90–100)
   - B (70–89)
   - C (50–69)
   - F (below 50)

9. Membership Username Check

   A list contains registered usernames. Check if "Lostboy" is registered.

10. Delivery Fee Calculator

   If distance is:

   - under 5km → $2
   - 5–15km → $5
   - above 15km → $10

🎯 Mini Project (Today)

🏧 ATM Withdrawal Program

Ask the user for:

- account balance
- withdrawal amount

Rules:

If withdrawal ≤ balance → Allow
Else → Decline

---

✅ Next Lesson

In the next chapter, we will learn:

- Loops (for, while)
- Nested Conditions
- Real-world Python Projects

📌 Author: Remy Ashimirwe
📚 Course: Python Programming for Beginners


Welcome to this Python learning repository!  
This project is designed to teach **Python programming step by step** using
clear explanations, real examples, and hands-on practice.


Whether you're a complete beginner or refreshing your skills, this repo
will help you build a strong Python foundation.


---


## 🎯 Who Is This For?


- Beginners with **no programming experience**
- Students learning Python for school or self-study
- Anyone who wants to understand Python **by writing code**


---


## 📚 What You Will Learn


- Python syntax and indentation
- Variables and data types
- Conditional statements (`if / else`)
- Loops (`for`, `while`)
- Functions
- Lists, tuples, dictionaries
- Basic problem-solving with Python


---


## 🗂 Repository Structure



python-course/
│
├── 01_basics/
│ ├── variables.py
│ ├── data_types.py
│
├── 02_conditions/
│ └── if_else.py
│
├── 03_loops/
│ ├── for_loop.py
│ └── while_loop.py
│
├── 04_functions/
│ └── functions.py
│
└── exercises/
└── practice_tasks.py



---


## ▶️ How to Use This Repository


1. Install Python (version 3.8+ recommended)
2. Clone the repository:
   ```bash
   git clone https://github.com/Remyashimirwe/pwd.git

Open files in VS Code or any Python editor

Read comments carefully and run the code:

python filename.py

Experiment and modify the code 🚀
## The for Loop
### 🔁 1️⃣ Used when you know how many times to repeat.
#### ✅ Basic Example
``` python
foods = ["apple", "banana", "mango", "cabbage", "rice"]
for food in foods:
    print(food)
```
### 🔄 2️⃣ The while Loop
Used when you don’t know how many times it will repeat.

###  try this
Check Even and Odd Numbers 1-100 
### Simple Banking System

Write a Python program that simulates a simple banking system with the following features:

The program starts with an initial balance of 1000.

It should repeatedly show a menu with these options:

1. Check Balance

2. Deposit

3. Withdraw

4. Exit

If the user chooses:

Check Balance → Display the current balance.

Deposit → Ask the user for an amount, add it to the balance, and confirm the deposit.

Withdraw → Ask the user for an amount. If the amount is less than or equal to the balance, subtract it and confirm the withdrawal. Otherwise, show "Insufficient balance".

Exit → Print "Thank you!" and stop the program.

### Number Guessing Game

Write a Python program that asks the user to guess a secret number between 1 and 10.

The program should work as follows:

Store a secret number (for example, secret = 7).

Continuously ask the user to enter a guess.

If the guess is equal to the secret number → print "Correct! 🎉" and stop the program.

If the guess is lower than the secret number → print "Too low!".

If the guess is higher than the secret number → print "Too high!".

The program should keep running until the user guesses correctly.

### practices exercises

1, Print numbers from 1 to 100.

2, Print only multiples of 3.

3, Create a login system with 3 attempts only.

4, Create a multiplication table from 1–10.

math.acos()	Returns the arc cosine of a number

math.acosh()	Returns the inverse hyperbolic cosine of a number

math.asin()	Returns the arc sine of a number

math.asinh()	Returns the inverse hyperbolic sine of a number

math.atan()	Returns the arc tangent of a number in radians

math.atan2()	Returns the arc tangent of y/x in radians

math.atanh()	Returns the inverse hyperbolic tangent of a number

math.ceil()	Rounds a number up to the nearest integer

math.comb()	Returns the number of ways to choose k items from n items without repetition and order

math.copysign()	Returns a float consisting of the value of the first parameter and the sign of the second parameter

math.cos()	Returns the cosine of a number

math.cosh()	Returns the hyperbolic cosine of a number

math.degrees()	Converts an angle from radians to degrees

math.dist()	Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point

math.erf()	Returns the error function of a number

math.erfc()	Returns the complementary error function of a number

math.exp()	Returns E raised to the power of x

math.expm1()	Returns Ex - 1

math.fabs()	Returns the absolute value of a number

math.factorial()	Returns the factorial of a number

math.floor()	Rounds a number down to the nearest integer

math.fmod()	Returns the remainder of x/y

math.frexp()	Returns the mantissa and the exponent, of a specified number

math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)

math.gamma()	Returns the gamma function at x

math.gcd()	Returns the greatest common divisor of two integers

math.hypot()	Returns the Euclidean norm

math.isclose()	Checks whether two values are close to each other, or not

math.isfinite()	Checks whether a number is finite or not

math.isinf()	Checks whether a number is infinite or not

math.isnan()	Checks whether a value is NaN (not a number) or not

math.isqrt()	Rounds a square root number downwards to the nearest integer

math.ldexp()	Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i

math.lgamma()	Returns the log gamma value of x

math.log()	Returns the natural logarithm of a number, or the logarithm of number to base

math.log10()	Returns the base-10 logarithm of x

math.log1p()	Returns the natural logarithm of 1+x

math.log2()	Returns the base-2 logarithm of x

math.perm()	Returns the number of ways to choose k items from n items with order and without repetition

math.pow()	Returns the value of x to the power of y

math.prod()	Returns the product of all the elements in an iterable

math.radians()	Converts a degree value into radians

math.remainder()	Returns the closest value that can make numerator completely divisible by the denominator

math.sin()	Returns the sine of a number

math.sinh()	Returns the hyperbolic sine of a number

math.sqrt()	Returns the square root of a number

math.tan()	Returns the tangent of a number

math.tanh()	Returns the hyperbolic tangent of 
a number

math.trunc()	Returns the truncated integer parts of a number
Math Constants
Constant	Description

math.e	Returns Euler's number (2.7182...)

math.inf	Returns a floating-point positive infinity

math.nan	Returns a floating-point NaN (Not a Number) value

math.pi	Returns PI (3.1415...)

math.tau	Returns tau (6.2831...)

# ARRAY
## 🛒 1. Supermarket Shopping System

A supermarket stores daily sales amounts in a list:

[12000, 8500, 4300, 15000, 9800, 6000]

Tasks:

Display all sales amounts using a loop.

Find and display sales greater than 10,000.

Count how many days had sales below 7,000.

Find the highest and lowest sale.

Display only even sales amounts.

# Tuples
A tuple is an ordered, immutable collection of items. Once created, you cannot change its contents.
Creating tuples:
python# Empty tuple
empty_tuple = ()

# Tuple with items
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Single item tuple (note the comma!)
single = (42,)

# Without parentheses
point = 10, 20, 30
Key characteristics:

Immutable - cannot add, remove, or change items
Ordered - items maintain their position
Allow duplicates
Can contain mixed data types

Common operations:
pythonmy_tuple = (1, 2, 3, 4, 5)

# Accessing items
print(my_tuple[0])        # 1
print(my_tuple[-1])       # 5

# Slicing
print(my_tuple[1:3])      # (2, 3)

# Length
print(len(my_tuple))      # 5

# Unpacking
x, y, z = (10, 20, 30)

# Count and index
numbers = (1, 2, 2, 3, 2)
print(numbers.count(2))   # 3
print(numbers.index(3))   # 3
Dictionaries
A dictionary is an unordered collection of key-value pairs. It's mutable and very useful for storing related data.
Creating dictionaries:
python# Empty dictionary
empty_dict = {}

# Dictionary with items
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using dict()
another = dict(name="Bob", age=25)
Common operations:
pythonstudent = {"name": "John", "grade": 85, "major": "CS"}

# Accessing values
print(student["name"])           # John
print(student.get("age", 0))     # 0 (default if key doesn't exist)

# Adding/modifying
student["age"] = 20              # Add new key
student["grade"] = 90            # Modify existing

# Removing
del student["major"]             # Delete key
grade = student.pop("grade")     # Remove and return value

# Checking keys
if "name" in student:
    print("Name exists")

# Getting all keys, values, items
print(student.keys())            # dict_keys(['name', 'age'])
print(student.values())          # dict_values(['John', 20])
print(student.items())           # dict_items([('name', 'John'), ('age', 20)])

# Looping
for key, value in student.items():
    print(f"{key}: {value}")

## Practice Exercises
## Easy Exercises
Exercise 1: Create a tuple with your favorite 5 movies and print the first and last movie.

Exercise 2: Create a dictionary representing a book with keys: title, author, year, pages. Print all the information.

Exercise 3: Given the tuple numbers = (10, 20, 30, 40, 50), unpack it into 5 separate variables and print them.
Medium Exercises

Exercise 4: Write a program that counts how many times each word appears in a sentence using a dictionary.
pythonsentence = "hello world hello python world"
# Expected output: {'hello': 2, 'world': 2, 'python': 1}

Exercise 5: Create a dictionary of student grades. Calculate and print the average grade.
pythongrades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}

Exercise 6: Given a list of tuples representing coordinates, find the point closest to the origin (0, 0).
pythonpoints = [(3, 4), (1, 1), (5, 12), (2, 2)]
# Hint: Use distance formula: sqrt(x² + y²)
Challenging Exercises
Exercise 7: Create a phone book program with a dictionary. It should allow users to:

Add a contact (name and phone number)
Search for a contact by name
Delete a contact
Display all contacts

Exercise 8: You have a list of tuples with (name, score). Create a dictionary where keys are score ranges ("90-100", "80-89", etc.) and values are lists of names in that range.
pythonstudents = [("Alice", 95), ("Bob", 82), ("Charlie", 78), ("Diana", 91)]
Exercise 9: Create a nested dictionary representing a library catalog with books organized by genre. Each book should have: title, author, and year. Write functions to:

Add a book to a genre
Search for books by author
List all books in a specific genre
