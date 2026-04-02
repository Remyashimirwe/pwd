def count_frequencies(items):
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
print(count_frequencies(["e", "a", "o", 12, 12,12]))
student_list = ["benz", "benz", "benz", "benz", "benz", "benz", "benz", "benz", "benz", "benz"]
change = input("enter the new brand: ")
student_list[0] = change
print(student_list)