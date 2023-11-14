# Upload BOJ Gold-5 Deque & implement 21610번 마법사 상어와 비바라기
from collections import deque
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
removedCloud = [[0 for _ in range(N)] for _ in range(N)]
clouds = deque([[N-2,0],[N-2,1],[N-1,0],[N-1,1]])

def moveClouds(way, move):
    x, y = 0, 0
    if way == 1:
        y -= 1
    elif way == 2:
        x -= 1
        y -= 1
    elif way == 3:
        x -= 1
    elif way == 4:
        x -= 1
        y += 1
    elif way == 5:
        y += 1
    elif way == 6:
        x += 1
        y += 1
    elif way == 7:
        x += 1
    elif way == 8:
        x += 1
        y -= 1
    else:
        return
    x *= move
    y *= move
    for i in range(len(clouds)):
        nx, ny = clouds[i][0], clouds[i][1]
        nx += x
        ny += y
        if nx < 0:
            num = (abs(nx) % N)
            if num:
                nx = N-num
            else:
                nx = num
        else:
            nx = nx % N
        if ny < 0:
            num = (abs(ny) % N)
            if num:
                ny = N-num
            else:
                ny = num
        else:
            ny = ny % N
        clouds[i][0] = nx
        clouds[i][1] = ny

def includeRain():
    
    for i in range(len(clouds)):
        x, y = clouds[i][0], clouds[i][1]
        maps[x][y] += 1
        removedCloud[x][y] = 1
    
    while clouds:
        x, y = clouds.popleft()
        for way in [[-1,-1],[-1,1],[1,-1],[1,1]]:
            nx = x + way[0]
            ny = y + way[1]
            
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny]:
                maps[x][y] += 1
        

def createCloud():
    for i in range(N):
        for j in range(N):
            if maps[i][j] >= 2 and not removedCloud[i][j]:
                maps[i][j] -= 2
                clouds.append([i,j])

def init():
    for i in range(N):
        for j in range(N):
            removedCloud[i][j] = 0


for _ in range(M):
    way, move = map(int, input().split())
    moveClouds(way, move)
    includeRain()
    createCloud()
    init()

answer = 0
for i in range(N):
    answer += sum(maps[i])
print(answer)
