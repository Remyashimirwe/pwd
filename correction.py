## unpackaging the dictionary
person = {"fname": "Kali joo", "age": "20"}
def perso_info(fname, age):
    print(f"hello {fname} you are {age} years old")
perso_info(**person)

number = (20,30,40)
def add(*a):
    print(a[1])
add(*number)
# combining the *args and **kwargs
def myfunction(title, *args, **kwargs):
    print("Title", title)
    print("Age", args)
    print("fname",kwargs)
myfunction("user_info",15, age=15 , fname= "King")
