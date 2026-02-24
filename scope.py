# local scope and global scope 
y = 10
x= 30
def myfanc(x,y):
     #local scope
    global z
    z = 20
    return x + y
result=myfanc(x,y)
print(result)
print(z)
def  add():
    x= "jane"
    def greeting():
        nonlocal x
        x= "hello world"
    greeting()
    return x
res = add()
print(res)
# multiply a local valiable with the global

num3 = 15 #global
def multiply():
    global num1
    num1 = 30 # global
    num2 = 40 #local
    return num1*num2
resul = multiply()
print(resul)
print(num1)
print(num3)
 