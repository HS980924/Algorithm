# Upload Gold-3 BFS 다리 만들기
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]
border = []
ways = [[0,1],[1,0],[-1,0],[0,-1]]
answer = N*N

def changeMaps(x,y,irelandNum):
    borderTmp = []
    queue = deque()
    queue.append([x,y])
    
    while queue:
        x, y = queue.popleft()
        maps[x][y] = irelandNum
        tmpCnt = 0
        
        for i in range(4):
            nx, ny = x+ways[i][0], y+ways[i][1]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not maps[nx][ny]:
                    tmpCnt =+ 1
                if not visited[nx][ny] and maps[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx,ny])
                    
        if tmpCnt:
            borderTmp.append([x,y])

    return borderTmp

irelandNum = 1
for i in range(N):
    for j in range(N):
        if maps[i][j] and not visited[i][j]:
            border.append(changeMaps(i,j,irelandNum))
            irelandNum += 1

def minDistance(borderList, curr_Ireland):
    result = N*N
    visited = [[0]*(N) for _ in range(N)]
    queue = deque()
    
    for x in borderList:
        queue.append(x)
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x+ways[i][0], y+ways[i][1]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and not maps[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                if maps[nx][ny] > curr_Ireland and result > visited[x][y]:
                    result = visited[x][y]
                    return result

for i in range(len(border)-1):
    answer = min(answer, minDistance(border[i],i+1))

print(answer)
