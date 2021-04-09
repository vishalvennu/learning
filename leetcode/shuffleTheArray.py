nums = [1,2,3,4,5,6]
n = int(len(nums)/2)
nums_New = []

for i in range(0,n,1):
    nums_New.append(nums[i])
    nums_New.append(nums[i+n])
print(nums_New)