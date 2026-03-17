# Python Module Exercise  
Below is a complete exercise you can give to students — or use yourself — to practice creating, importing, and using modules.

---

##  **Step 1 — Create a Module (`mymath.py`)**

Save this file as **mymath.py**:

```python
# mymath.py

# A simple function that adds two numbers
def add(a, b):
    return a + b

# A function that multiplies two numbers
def multiply(a, b):
    return a * b

# A dictionary stored inside the module
info = {
    "topic": "Basic Math Module",
    "version": 1.0,
    "author": "Remy"
}
```

---

##  **Step 2 — Use the Module (`main.py`)**

Create another file named **main.py**:

```python
# main.py

import mymath

# Using functions from the module
result1 = mymath.add(10, 5)
result2 = mymath.multiply(4, 7)

print("Addition:", result1)
print("Multiplication:", result2)

# Accessing the dictionary inside the module
print("Module Info:", mymath.info)
```

---

## **Step 3 — Exercise Tasks**

Ask the student to:

1. Create the module `mymath.py` with:
   - Two functions (`add`, `multiply`)
   - One dictionary (`info`)
2. Import the module in `main.py`
3. Call the functions and print the results
4. Access and print the dictionary values
5. Create an alias for the module:

```python
import mymath as mx
print(mx.add(3, 9))
```

6. Use `dir()` to list everything inside the module:

```python
print(dir(mymath))
```

---

## **Bonus Question**  
**True or False:** A module can only contain one function or object.  