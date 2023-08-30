nums = [-1,1,0,-3,3]
result = [1]*len(nums)
prefix = [1]*len(nums)
suffix = [1]*len(nums)
temp = 1
for i in range(len(nums)):
    temp = temp * nums[i]
    prefix[i] = temp 
temp = 1
for i in range(len(nums)-1,-1,-1):
    temp = temp * nums[i]
    suffix[i] = temp
temp = 0
for i in range(len(nums)):
    if i==0:
        result[i] = temp + suffix[i+1]
    elif i == len(nums) - 1:
        result[i] = prefix[i-1] + temp
    else:
        result[i] = prefix[i-1] + suffix[i+1]
print(result)        