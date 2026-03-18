class Person:
    def __init__(self, name, age = 15):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello welcome again, {self.name}")
    def grow(self):
        self.age += 1
        print(f"you age is {self.age}")

p1 = Person("user_name")
print(p1.greet(), p1.grow())

class Calculator:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def multi(self):
        return self.a * self.b
calc = Calculator(5,6)
del Calculator.add
print(calc.add())
print(calc.multi())

#__str__()
class Students:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    def __str__(self):
        return f"welcome to our school {self.name} you are in level {self.level}"
s1 = Students("rexy", 12)
print(s1)
