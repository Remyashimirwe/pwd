class person:
    def __init__(self, name, age = 15):
        self.name = name
        self.age = age
p1 = person("remy")
p2 = person("Alice" , 20)
print(p1.name, p1.age)
print(p2.name, p2.age)