def permute(nums):
        res = [[]]
        
        for num in nums:
            length = len(res)
            for i in range(length):
                subset = res[i]
                for j in range(len(subset)):
                    res.append(subset[:j] + [num] + subset[j:])
                subset.append(num)
        return res
nums = [1,2,3]
print(permute(nums))