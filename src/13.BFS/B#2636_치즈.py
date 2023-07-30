# Upload BOJ Gold-5 BFS 치즈
from collections import deque
N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
ways = [[0,1],[1,0],[-1,0],[0,-1]]
time, cnt = 0, 0

def bfs():
    q = deque([[0,0]])
    cheeze_melt = []
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx, ny = x+ways[i][0], y+ways[i][1]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if maps[nx][ny] == 0:
                    q.append([nx,ny])
                if maps[nx][ny] == 1:
                    cheeze_melt.append([nx,ny])
    
    for x,y in cheeze_melt:
        maps[x][y] = 0
        
    return len(cheeze_melt)

while True:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    meltCnt = bfs()
    if meltCnt:
        cnt = meltCnt
    else:
        print(time)
        print(cnt)
        break
    time += 1
    
