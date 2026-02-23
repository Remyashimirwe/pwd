# Python Iterators
marks = [10,20,304,5,60]
marks[1] = "hei"
print(marks)
# the iterator protocol 
# - iter()
# - __next__()
#for x in marks:

# this how we use the __next__() and also iter()
   #iterator = iter(x)
   #next = __next__(iterator)
# iterable and iterator
# objects which is iterable
# -lists
# -tuples
# -Dictionaries
# -Sets
# -Map 
# iterator 
# iter()
my_list  = (1,2,3)
it = iter(my_list)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

for num in Counter(1, 5):
    print(num)
