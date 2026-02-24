# hnadleing the error  
x= int(input("enter the number you wnat to divide: "))
y = int(input("enter the divisior: "))
if y == 0:
    print("zero can not be a divisor")   
else:
    result = x/y
    print(result)
# lambda

x = lambda a, b: a+b+10
print(x(30,40))
