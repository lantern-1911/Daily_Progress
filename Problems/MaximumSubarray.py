nums = [-2,1,-3,4,-1,2,1,-5,4]
curr_sum = 0
maxi = nums[0]
for i in nums:
    if curr_sum<0:
        curr_sum = 0
    curr_sum+= i
    maxi = max(curr_sum,maxi)    
print(maxi)