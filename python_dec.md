# **📘 Full Lecture: Python Decorators (Beginner → Advanced)**

## **1. Introduction**
In Python, **decorators** allow you to *extend or modify* the behavior of a function **without changing its original code**.  
They are one of the most powerful and elegant features in Python, widely used in:

- Web frameworks (Flask, Django)
- Logging
- Authentication
- Performance measurement
- Caching
- Access control
- API rate limiting

A decorator is simply:

> **A function that takes another function as input and returns a new function.**

---

# **2. Why Do We Need Decorators?**
Imagine you want to add extra behavior to many functions:

- Convert output to uppercase  
- Log when the function is called  
- Check user permissions  
- Measure execution time  

You could rewrite each function…  
But that violates **DRY** (Don’t Repeat Yourself).

Decorators solve this by letting you “wrap” a function with extra behavior.

---

# **3. Basic Decorator Structure**

```python
def decorator_name(func):
    def wrapper():
        # extra behavior
        return func()
    return wrapper
```

Apply it using:

```python
@decorator_name
def myfunction():
    ...
```

This is equivalent to:

```python
myfunction = decorator_name(myfunction)
```

---

# **4. Example 1 — Simple Uppercase Decorator**

```python
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

print(myfunction())
```

**Key idea:**  
`myfunction()` is replaced by `myinner()`, which calls the original function and modifies the result.

---

# **5. Using the Same Decorator on Multiple Functions**

```python
@changecase
def myfunction():
    return "Hello Sally"

@changecase
def otherfunction():
    return "I am speed!"
```

Each function is wrapped independently.

---

# **6. Decorating Functions With Arguments**
Your wrapper must accept the same arguments as the original function.

```python
def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase
def myfunction(nam):
    return "Hello " + nam

print(myfunction("John"))
```

---

# **7. Using *args and **kwargs**
When you don’t know the number or type of arguments:

```python
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner
```

This makes your decorator **universal**.

---

# **8. Decorators With Their Own Arguments**
This is called a **decorator factory**.

```python
def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                return func().lower()
            else:
                return func().upper()
        return myinner
    return changecase

@changecase(1)
def myfunction():
    return "Hello Linus"
```

Here:

- `changecase(1)` returns a decorator  
- That decorator wraps the function  

---

# **9. Multiple Decorators on One Function**
Decorators stack from **bottom to top**.

```python
@decoratorA
@decoratorB
def func():
    ...
```

Execution order:

1. `decoratorB` wraps `func`
2. `decoratorA` wraps the result of step 1

Example:

```python
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

@changecase
@addgreeting
def myfunction():
    return "Tobias"
```

---

# **10. Preserving Function Metadata**
Decorators replace the original function with the wrapper.  
This causes metadata loss:

```python
print(myfunction.__name__)
```

It prints `"myinner"` instead of `"myfunction"`.

### **Solution: functools.wraps**

```python
import functools

def changecase(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner
```

Now metadata is preserved.

---

# **11. Real‑World Use Cases**
Here are practical examples you can teach your students:

### **Logging**
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

### **Authentication**
```python
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            return "Access denied"
        return func(user)
    return wrapper
```

### **Timing**
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Time:", time.time() - start)
        return result
    return wrapper
```

---

# **12. Summary Table**

| Concept | Meaning |
|--------|---------|
| Decorator | Function that wraps another function |
| `@decorator` | Syntactic sugar for function wrapping |
| Wrapper function | Inner function that adds behavior |
| `*args, **kwargs` | Allows flexible arguments |
| Decorator with arguments | Requires 3 nested functions |
| Multiple decorators | Applied bottom → top |
| `functools.wraps` | Preserves metadata |

---

# **13. Final Takeaway**
Decorators are one of Python’s most elegant tools.  
They allow you to:

- Add behavior  
- Reuse logic  
- Keep code clean  
- Avoid repetition  
- Build powerful abstractions  

Once you master decorators, you unlock a deeper level of Python programming.