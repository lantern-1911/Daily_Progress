def updateMatrix(mat):
        row = len(mat)
        column = len(mat[0])
        visited = []
        for i in range(row):
            for j in range(column):
                if mat[i][j] == 0:
                    visited.append((i,j))
                elif mat[i][j] == 1:
                    mat[i][j] = '*'
        diagonals = [[0,-1],[0,1],[-1,0],[1,0]]
        for i,j in visited:
            for k,v in diagonals:
                nr = i + k
                nc = j + v
                if nr in range(row) and nc in range(column) and mat[nr][nc]=='*':
                    mat[nr][nc] = mat[i][j] + 1
                    visited.append((nr,nc))
        return mat            
mat = [[0,0,0],[0,1,0],[0,0,0]]
print(updateMatrix(mat))
