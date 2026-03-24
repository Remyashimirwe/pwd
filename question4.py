class Patient:
    hospital_name = "DMC hospital"
    def __init__(self, name, _age):
        self.name = name
        self._age = _age
    def get_age(self):
        return f"you are are {self._age} years old"
    def set_age(self, new_age):
        self._age = new_age
        return f"new age {self._age}"
p1 = Patient("Remy", 19)
p2 = p1.get_age()
print(p1.name, p1._age)
print(p2)
print(p1.set_age(35))

