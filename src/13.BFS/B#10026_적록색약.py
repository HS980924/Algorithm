import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [ list(input().strip()) for _ in range(N) ]

ways = [[-1,0], [0,1], [1,0], [0,-1]]
RB = {'R':0, 'G':0 ,'B':1}

RGB_person = [[0 for _ in range(N)] for _ in range(N)]
RB_person = [[0 for _ in range(N)] for _ in range(N)]

RGB_cnt = 1
RB_cnt = 1

queue = deque()
queue2 = deque()

for i in range(N):
    for j in range(N):
        if not RB_person[i][j]:
            RB_person[i][j] = RB_cnt
            queue.append([i,j])
            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    nx, ny = x+ways[k][0], y+ways[k][1]
                    
                    if 0 <= nx < N and 0 <= ny < N:
                        if not RB_person[nx][ny]:
                            if RB[board[x][y]] == RB[board[nx][ny]]:
                                RB_person[nx][ny] = RB_cnt
                                queue.append([nx,ny])
            RB_cnt += 1
            
        if not RGB_person[i][j]:
            RGB_person[i][j] = RGB_cnt
            queue2.append([i,j])
            while queue2:
                x, y = queue2.popleft()
                
                for k in range(4):
                    nx, ny = x+ways[k][0], y+ways[k][1]
                    
                    if 0 <= nx < N and 0 <= ny < N:
                        if not RGB_person[nx][ny]:
                            if board[x][y] == board[nx][ny]:
                                RGB_person[nx][ny] = RGB_cnt
                                queue2.append([nx,ny])
            RGB_cnt += 1
    
print(RGB_cnt-1, RB_cnt-1)
