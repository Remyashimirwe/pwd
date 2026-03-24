class student:
    school_name = "future focus academy"
    def __init__(self, name ,grade):
        self.name = name
        self.grade = grade
s1 = student("King", "grade 10")
s1.email = "king@gmail.com"
s1.age = 17
school_name = "mt kigali school"
print(f"name: {s1.name}")
print(f"grade: {s1.grade}")
print(f"email: {s1.email}")
print(f"age: {s1.age}")

del s1.age
print(f"age: {s1.age}")
