def fun(i,j):
    grid[i][j] = "2"
    for k,v in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = i + k
        nc = j + v
        if nr in range(r) and nc in range(c) and grid[nr][nc] == "1":
            fun(nr,nc)

grid =  [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]           
r = len(grid)
c = len(grid[0])
island=0
for i in range(r):
    for j in range(c):
        if grid[i][j] == "1":
            island += 1
            fun(i,j)
print(island)            