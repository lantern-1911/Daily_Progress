n = int(input("enter no of elements:"))
nums = [int(i) for i in input().split()][0:n]
print(nums)
d = dict()
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
sorted_d = dict(sorted(d.items(), key = lambda x:x[1],reverse = True))
print(list(sorted_d.keys())[0])