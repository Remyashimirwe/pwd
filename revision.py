from functools import reduce
def process_numbers(nums):
    even = []
    odd = []
    squares = []
    greater_than_10 = []

    it = iter(nums)
    iterator_first_three = []
    for i in range(3):
        try:
            iterator_first_three.append(next(it))
        except StopIteration:
            break;
    for n in nums:
        if n%2 == 0:
            even.append(n)
        elif(n%2 !=0):
            odd.append(n)
        squares.append(n*n)
        if n >10: 
            greater_than_10.append(n)
    lambda_sum = reduce(lambda a, b: a+b , nums)
    dict ={
        "even":even,
        "odd": odd,
        "squares": squares,
        "greater_than_10": greater_than_10,
        "iterator_first_three": iterator_first_three,
        "lambda_sum": lambda_sum
    } 
    return dict["greater_than_10"]  
nums = [21,20,30,405,60,80,97]
print(process_numbers(nums)) 


