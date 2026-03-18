class Person:
    def __init__(self, name, age =6):
        self.name = name
        self.age = age
    def info(self):
        print(f"your name is {self.name}")
students = [{"name":"Remy", "age": 15},
            {"name": "king", "age" :19}
            ]
for student in students:
    p1 = Person(student["name"], student["age"])
    print(p1.age)
    print(p1.name)
p2= Person("bigboy")
p3 = p1.info()
print(p2.age, p2.name, p3)
#class Person:
 #   pass
#p1 = Person()
#p1.name = "remy"
#p1.age = 15
#print(p1.age)
#print(p1.name)
