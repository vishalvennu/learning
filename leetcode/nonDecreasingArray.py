nums = [4,2,3]

c = 0
for i in range(0,len(nums)-1):
    if (nums[i] > nums[i+1]):
        c += 1

if(c>1):
    print ("False")
else:
    print("True") 
