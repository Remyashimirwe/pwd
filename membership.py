def changecase(func):
    def mychange(x):
        return func(x).upper()
    return mychange
@changecase
def myfuction(nam):
    return "hello " + nam
name = input("please enter the name: ")
print(myfuction(nam))