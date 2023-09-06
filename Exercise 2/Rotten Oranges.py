def rottenOranges(grid):
    r = len(grid)
    c = len(grid[0])
    p = 0
    visited = ()
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                visited.append((i,j))
    while visited:
        x,y = visited.popleft()
        for k,v in [[-1,0],[1,0],[0,1],[0,-1]]:
            nr = x + k
            nc = y + v
            if nr in range(r) and nc in range(c) and grid[nr][nc] == 1:
                grid[nr][nc] = grid[x][y] + 1
                visited.append((nr,nc))
                    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                return -1
            p = max(p, grid[i][j])
    return max(p-2,0)

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(rottenOranges(grid))
