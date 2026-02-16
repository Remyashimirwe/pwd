amounts = [12000, 8500, 4300, 15000, 9800, 6000]
print("Count how many days had sales below 7,000: ")
count_times = 0
for amount in amounts:
    if amount <7000:
        print(amount)
        count_times += 1
print(count_times)
highest= max(amounts)
lowest = min(amounts)
print(f"the highest is : {highest}")
print(f"the lowest is {lowest}")
print("Display only even sales amounts.")
for amount in amounts:
    if amount % 2 == 0:
        print(amount)