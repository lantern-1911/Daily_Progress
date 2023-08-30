intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = sorted(intervals + [newInterval])
result = [intervals[0]]
for i in range(1,len(intervals)):
    if result[-1][1] >= intervals[i][0]:
        result[-1][1] = max(result[-1][1],intervals[i][1])
    else:
        result.append(intervals[i])  
print(result)