# import sys
# N = int(sys.stdin.readline())
# board = [["*" for i in range(N)] for _ in range(N)]

# def solution(N):
#     cnt = exponent(N)
#     for x in range(cnt):
#         for i in range(N):
#             for j in range(N):
#                 if i // 3**x % 3 == 1 and j // 3**x % 3 == 1:
#                     board[i][j] = ' '
                    
#     for tmp in board:
#         for value in tmp:
#             print(value,end='')
#         print()

# def PRINT(N):
#     solution(N)
#     for tmp in board:
#         for value in tmp:
#             print(value,end='')
#         print()
# PRINT(N)

import sys
N = int(sys.stdin.readline())
board = [[" " for i in range(N)] for _ in range(N)]

def solution(N,x,y):
    if N == 3:
        for i in range(x,x+3):
            for j in range(y,y+3):
                if i % 3 == 1 and j % 3 == 1:
                    continue
                else:
                    board[i][j] = "*"
    else:
        a = N//3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    solution(a,x+i*a,y+j*a)

def PRINT(N):
    solution(N,0,0)
    for tmp in board:
        for value in tmp:
            print(value,end='')
        print()
        
PRINT(N)