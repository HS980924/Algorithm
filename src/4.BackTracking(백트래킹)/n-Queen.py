
# def solution(n):
#     global board
#     board = [[0 for _ in range(n)] for _ in range(n)]
#     answer = backTracking(0, n)
#     return answer


# def backTracking(cnt, n):
#     if cnt == n:
#         return 1
#     else:
#         result = 0
#         for i in range(n):
#             if checking(cnt, i, n):
#                 board[cnt][i] = 1
#                 result += backTracking(cnt+1, n)
#                 board[cnt][i] = 0
                
#         return result

# def checking(row, col, n):
#     # 가로 체크
#     for i in range(n):  
#         if 1 in board[row]:
#             return False
        
#     # 세로 체크
#     for i in range(n):
#         if board[i][col]:
#             return False
    
    
#     # 대각선 체크 우상향
#     x = row
#     y = col
#     while x >= 0 and y < n:
#         if board[x][y]:
#             return False
#         x -= 1
#         y += 1
    
#     # 대각선 체크 우하향
#     x = row
#     y = col
#     while x < n and y < n:
#         if board[x][y]:
#             return False
#         x += 1
#         y += 1
    
#     x = row
#     y = col
#     # 대각선 체크 좌하향
#     while x < n and y >= 0:
#         if board[x][y]:
#             return False
#         x += 1
#         y -= 1
    
#     # 대각선 체크 좌상향
#     x = row
#     y = col
#     while x >= 0 and y >= 0:
#         if board[x][y]:
#             return False 
#         x -= 1
#         y -= 1
        
#     return True

# def solution(n):
#     answer = 0
#     global board
#     board = [-1]*n
#     answer = backTracking(0, n)
#     return answer

# def checkBoard(x, y):
#     for i in range(y):
#         if abs(x-board[i]) == 0 or abs(x-board[i]) == abs(y-i):
#             return False
#     return True

# def backTracking(idx, n):
#     if idx == n:
#         return 1
#     else:
#         result = 0
#         if not idx:
#             for value in range(n):
#                 board[idx] = value
#                 result += backTracking(idx+1,n)
#         else:
#             for value in range(n):
#                 if checkBoard(value, idx):
#                     board[idx] = value
#                     result += backTracking(idx+1,n)
                    
#         return result
# print(solution(4))

def solution(n):
    answer = 0
    global board
    board = [-1]*n
    for i in range(n):
        board[0] = i
        answer += nqueen(1,n)
    return answer

def nqueen(x,n):
    if x == n:
        return 1
    else:
        result = 0
        for y in range(n):
            check = True
            for x2 in range(x):
                if y == board[x2] or abs(y-board[x2]) == abs(x-x2):
                    check = False
                    break
            if check:
                board[x] = y
                result += nqueen(x+1,n)
                
        return result 
print(solution(4))
