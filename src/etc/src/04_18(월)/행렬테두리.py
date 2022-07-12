def PRINT(board):
    for x in board:
        print(x)
def solution(rows, columns, queries):
    answer = []
    board = [[ (i+1)+((j)*columns) for i in range(columns)] for j in range(rows)]
    
    for loc in queries:
        x, y = loc[0]-1, loc[1]-1
        bef = board[x][y]
        aft = board[x][y]
        arr = []
        
        while(y < loc[3]-1):
            aft = board[x][y+1]
            board[x][y+1] = bef
            bef = aft
            arr.append(aft)
            y += 1
            
        
        while(x < loc[2]-1):
            aft = board[x+1][y]
            board[x+1][y] = bef
            bef = aft
            arr.append(aft)
            x += 1
        
        while(y > loc[1]-1):
            aft = board[x][y-1]
            board[x][y-1] = bef
            bef = aft
            arr.append(aft)
            y -= 1
        
        while(x > loc[0]-1):
            aft = board[x-1][y]
            board[x-1][y] = bef
            bef = aft
            arr.append(aft)
            x -= 1
        
        answer.append(min(arr))
        
    
    return answer


r = 6
c = 6
q = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(r,c,q))