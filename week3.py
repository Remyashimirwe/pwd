def test(*args):
    print(args)

test(1, 2, 3)
def test(**kwargs):
    print(kwargs)

test(a=1, b=2)
def func(a, *args, **kwargs):
    print(a, args, kwargs)

func(10, 20, 30, x=5, y=7)
def combine(*args):
    return sum(args)

print(combine(1, 2, 3, 4))

def student_name(*args):
    print(args)

student_name(17,49,60,70)
a= 100
b= 200
def add(a, b,*args, **kwargs):
    print(a+b+sum(kwargs.values()))
add(a,b,apple= 100, milk= 200)