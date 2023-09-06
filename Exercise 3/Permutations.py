def permute(nums):
        res = [[]]
        
        for num in nums:
            length = len(res)
            for i in range(length):
                subset = res[i]
                print("subset:",subset)
                for j in range(len(subset)):
                    res.append(subset[:j] + [num] + subset[j:])
                    print("[:j]:",subset[:j])
                    print("num",num)
                    print("[j:]",subset[j:])
                    print("res:",res)
                subset.append(num)
        return res
nums = [1,2,3]
print(permute(nums))