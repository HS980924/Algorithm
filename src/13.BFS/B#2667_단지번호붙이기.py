# Upload Silver-1 BFS 단지번호붙이기
from collections import deque

N = int(input())
maps = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
ways = [[0,1],[1,0],[-1,0],[0,-1]]
answer = []

def cntApart(x,y):
    q = deque()
    q.append([x,y])
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x+ways[i][0], y+ways[i][1]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and maps[nx][ny] == "1":
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    cnt += 1
                    
    return cnt


for i in range(N):
    for j in range(N):
        if maps[i][j] == "1" and not visited[i][j]:
            visited[i][j] = 1
            answer.append(cntApart(i,j))

answer.sort()
print(len(answer))
for x in answer:
    print(x)