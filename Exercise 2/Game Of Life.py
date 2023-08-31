def countAdj(i,j,board):
    count=0
    li=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for a,b in li:
        row=i+a
        col=j+b
        if row>=0 and row<len(board) and col>=0 and col<len(board[0]):
            count+=board[row][col]
    return count

def gameOfLife(board):
    ans=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            val=countAdj(i,j,board)
            if val<2 or val>3:
                if board[i][j]!=0:
                    ans.append((i,j,0))
            elif val==3:
                if board[i][j]!=1:
                    ans.append((i,j,1))
    for (i,j,val) in ans:
        board[i][j]=val  

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))