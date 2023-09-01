m = int(input())
n = int(input())
res = [[0]*n]*(m-1)
res.append([1]*n)
for i in range(m-2,-1,-1):
    for j in range(n-1,-1,-1):
        if j == n-1:
            res[i][j] = 1
        else:
            res[i][j] = res[i][j+1] + res[i+1][j]
print(res[0][0])            