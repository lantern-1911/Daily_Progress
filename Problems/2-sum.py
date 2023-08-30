nums = [2,7,11,15]
target = 9
a = 0
for i in range(len(nums)):
    p = target-nums[i]
    if p in nums:
        a = nums.index(p)
        if a == i:
            continue
        break
print([i,a])    