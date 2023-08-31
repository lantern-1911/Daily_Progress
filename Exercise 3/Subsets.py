input = [1,2,3,4]
result = [[]]
for i in range(len(input)):
    result += [lst + [i] for lst in result]
print(result)