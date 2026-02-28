def changecase(func):
    def mychange(x):
        return func(x).upper()
    return mychange
@changecase
def myfuction(nam):
    return "hello " + nam
nam = input("please ente the name: ")
print(myfuction(nam))