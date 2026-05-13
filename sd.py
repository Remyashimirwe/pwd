nums = [3,2,4]
length = len(nums)
answer =[]
i=1
for j in range(length-1):
    for i in range(length-1):
        if nums[j]+nums[i] == 6:
            answer.append([i,j])
print(answer)