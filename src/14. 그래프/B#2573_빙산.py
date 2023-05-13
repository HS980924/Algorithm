import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1
    melted_maps = []
    
    while queue:
        x, y = queue.popleft()
        meltCnt = 0
        for k in range(4):
            nx, ny = x+ways[k][0], y+ways[k][1]
            
            if 0 <= nx < N and 0 <= ny < M:
                if not maps[nx][ny]:
                    meltCnt += 1
                else:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        queue.append([nx,ny])
        if meltCnt > 0:
            melted_maps.append([x,y,meltCnt])

    for x, y, meltCnt in melted_maps:
        maps[x][y] = max(0, maps[x][y]-meltCnt)
    
    return 1


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ways = [[1,0],[0,1],[-1,0],[0,-1]]
ices = []
year = 0

for i in range(N):
    for j in range(M):
            if maps[i][j]:
                ices.append((i,j))

while ices:
    cnt = 0
    visited = [ [0 for _ in range(M)]for _ in range(N)]
    delIces = []
    
    for i, j in ices:
        if maps[i][j] and not visited[i][j]:
            cnt += bfs(i,j)
        if not maps[i][j]:
            delIces.append((i,j))
    
    if cnt > 1:
        print(year)
        break
        
    ices = sorted(list(set(ices) - set(delIces)))
    year += 1

if cnt < 2:
    print(0)
