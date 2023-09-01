def canPartition(nums):
    if sum(nums)%2: return 0
    numSet = set([0])
    for i in nums:
        for j in list(numSet):
            numSet.add(i + j)
            if i + j == sum(nums)//2:
                return True
    return False

nums = [1,5,5,11]
print(canPartition(nums))