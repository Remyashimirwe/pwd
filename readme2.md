
---

# 🧠 Python `*args` and `**kwargs` — Question Bank

## 🔹 **Section 1: Conceptual Questions**
1. What is the purpose of using `*args` in a Python function?
2. What is the purpose of using `**kwargs` in a Python function?
3. How do `*args` and `**kwargs` differ in terms of the type of data they collect?
4. Can `*args` and `**kwargs` be used together in the same function? Explain how.
5. Why must `*args` come before `**kwargs` in a function definition?
6. What data types do `*args` and `**kwargs` store internally?
7. Explain what happens if you pass keyword arguments to a function that only accepts `*args`.
8. What is argument unpacking, and how does it relate to `*args` and `**kwargs`?

---

## 🔹 **Section 2: Code‑Based Questions**
### **Q1.** What is the output of the following code?
```python
def test(*args):
    print(args)

test(1, 2, 3)
```

### **Q2.** Predict the output:
```python
def test(**kwargs):
    print(kwargs)

test(a=1, b=2)
```

### **Q3.** What will this print?
```python
def func(a, *args, **kwargs):
    print(a, args, kwargs)

func(10, 20, 30, x=5, y=7)
```

### **Q4.** Identify the error:
```python
def wrong(**kwargs, *args):
    pass
```

### **Q5.** What is the output?
```python
def combine(*args):
    return sum(args)

print(combine(1, 2, 3, 4))
```

---

## 🔹 **Section 3: Application Questions**
1. Write a function that accepts any number of student names using `*args` and prints them.
2. Write a function that accepts any number of keyword arguments representing a student's profile (name, age, grade) using `**kwargs`.
3. Create a function that calculates the total price of items passed as keyword arguments (e.g., `apple=100`, `milk=500`).
4. Write a function that mixes both:
   - positional arguments  
   - variable positional arguments  
   - variable keyword arguments  
   and prints all three clearly.
5. Write a function that multiplies all numbers passed via `*args`.

---

## 🔹 **Section 4: Debugging Questions**
1. Why does this code fail?
```python
def func(*args, name):
    print(args, name)

func(1, 2, 3)
```

2. Fix the function so that it accepts both positional and keyword arguments:
```python
def func(a, b, **kwargs, *args):
    pass
```

3. What is wrong with this call?
```python
def f(**kwargs):
    print(kwargs)

f(1, 2, 3)
```

---

## 🔹 **Section 5: Real‑World Scenario Questions**
1. You are building a logging function that must accept any number of messages and any number of metadata fields. How would you design it using `*args` and `**kwargs`?
2. In a Django view, why might `*args` and `**kwargs` be used in the function signature?
3. How can `**kwargs` help when writing reusable class constructors?