
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

def solution(n):
    answer = 0
    board = [0]*(n+1)
    
    
    return answer
