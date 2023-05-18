# 2022.08.21(일)
# B#7569 < 토마토 > - BFS문제
# 문제 링크: https://www.acmicpc.net/status?user_id=choihs0924&problem_id=7569&from_mine=1

import sys
from collections import deque

M, N, H = map(int,sys.stdin.readline().split())
boxs = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)]for _ in range(H)]
#days = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dz = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]


def bfs():
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxs[i][j][k] == 1:
                    q.append([i,j,k])
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if boxs[nz][nx][ny] == 0:
                    boxs[nz][nx][ny] = boxs[z][x][y] + 1
                    q.append([nz,nx,ny])      
    
def searchMinValue():
    result = -1
    for x in boxs:
        for y in x:
            if 0 in y:
                return -1
            else:
                result = max(max(y),result)
                
    return result-1

bfs()
print(searchMinValue())
            
#print(searchMinValue())
    