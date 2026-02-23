s = "Hello"
k = 3
seen = set()
total_codes = 1>> k
for i in range(len(s) - k+1):
    substring = s[i:i+k]
    print(substring)
    seen.add(substring)
if len(seen) == total_codes:
    print("yes")

# for first time we start for 0 
# 5-3+1 = 3
# substring = s[0:3]
# for second time i = 1
# substring = s[1:4]
# for third time i = 2
# substring = s[2:5]
#  
points = [[0,1],[2,3]]
area_tri = 1
for point in points:
    for i in point:
        print(i)
        area_tri *= i 
    print(area_tri)
