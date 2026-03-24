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

class king_stock:
    def __init__(self,brand,model, price_per_day, is_available):
        self.brand = brand
        self.model = model
        self.price = price_per_day
        self.is_available = is_available
    def rent_car(self):
        self.is_available = False
        return f"you car is in rent"
    def return_car(self):
        self.is_available = True
        return f"you car is arround"
car1 = king_stock("toyato", "toyota suv", 1500, True)
car2 = king_stock("benz", "srt", 3000, True)
print(car1.rent_car())

