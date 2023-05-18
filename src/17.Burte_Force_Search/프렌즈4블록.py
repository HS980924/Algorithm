def solution(m, n, board):
    answer = 0
    board = list(list(x) for x in board)
    
    while True:
        loc_index = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != "-" and checking(i,j,board):
                    loc_index.append([i,j])
        
        for i in range(len(loc_index)):
            row = loc_index[i][0]
            col = loc_index[i][1]
            for x in range(row,row+2):
                for y in range(col,col+2):
                    if board[x][y] != "-":
                        answer += 1
                    board[x][y] = "-"
        
        
        for col in range(n):
            tmp = ""
            for row in range(m):
                if board[row][col] != "-":
                    tmp += str(board[row][col])
            cnt = 1
            for x in tmp[::-1]:
                board[m-cnt][col] = x
                cnt += 1
            
            while m-cnt > -1:
                board[m-cnt][col] = "-"
                cnt += 1

        if not loc_index:
            break
    
    return answer

def checking(x,y,board):
    tmp = board[x][y]
    for i in range(x,x+2):
        for j in range(y,y+2):
            if board[i][j] != tmp:
                return False
    
    return True
                

m = 6#4
n = 6#5
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"] #["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))