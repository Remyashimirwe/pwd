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
