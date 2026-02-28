# python opp
`classes` and `object` are two core concept in oop in python 

A `class` defines what an object should look like
while `object` is created based on that class.
## python class/objects
`class` is the blueprint of the object
### creating class
```python
class myclass:
    x = 5
```
you can create the object and use it to print the statement of the code
### creating object
```python
class myclass:
    x = 5
p1 = myclass()
print(p1)
```
so you can also delete using `del` method
```python
class myclass:
    x = 5
p1 = myclass()
del p1 
print(p1) # so this is going to return undefined becouse the p1 is deleted
```
but also we can create the multiple object
```python
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
```
note: each object is independent here
## Pass statement
we can use the `pass` when we created the class but we don't have the content yet 
```python
class mytest:
    pass
``` 
## Python method `__init__()`
the `__init__()` is executed when the class is being executed from the beginning, it also used to assign values to the object properties 
to perform necessary function 
```python
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("Remy", 19)
print(p1.name)
print(p1.age)
```
without using the `__init__()` you will have to set the method and the values by manual
```python
class person: 
    pass
p1 = person()
p1.name = "Remy"
p1.age = 15
print(p1.name)
print(p1.age)
```
so we can also set the default parameters in the function whenusing `__init__()`
```python
class person:
    def __init__(self, name, age = 15):
        self.name = name
        self.age = age
p1 = person("remy")
p2 = person("Alice" , 20)
print(p1.name, p1.age)
print(p2.name, p2.age)

```