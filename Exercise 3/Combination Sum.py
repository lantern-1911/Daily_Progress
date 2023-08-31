def combinationSum(candidates, target):
        res = []
        subset = []
        def backtrack(i):
            if sum(subset)==target:
                res.append(subset.copy())
                return
            elif sum(subset)>target:
                return
            else:
                for j in range(i,len(candidates)):
                    subset.append(candidates[j])
                    backtrack(j)
                    subset.remove(candidates[j])
        backtrack(0)
        return res
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))