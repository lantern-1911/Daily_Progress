from collections import Counter
def containsDuplicate( nums ):
        result = dict(Counter(nums))
        result=list(result.values())
        k = max(result)

        return True if k > 1 else False
nums = [1,2,3,2,3,1,2,2]
print(containsDuplicate(nums))
    
