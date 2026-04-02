### **Task: Build a Frequency Counter**
Create a function named `count_frequencies(items)` that takes a list of values and returns a dictionary showing how many times each unique value appears.

### Requirements
- The input will be a list containing strings, integers, or a mix of both.
- The output must be a dictionary where:
    - keys are the unique items from the list
    - values are the number of occurrences
- The function must not use `collections.Counter`.

### Example
```python
count_frequencies(["a", "b", "a", "c", "b", "a"])
# Output: {"a": 3, "b": 2, "c": 1}
```