# Upload BOJ Silver-1 BFS 2583번 영역 구하기
from collections import deque

M, N, K = map(int,input().split())

maps = [[1 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
areas = []
answer = 0

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1
    
    ways = [[0,1],[1,0],[-1,0],[0,-1]]
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for way in ways:
            nx, ny = x+way[0], y+way[1]
            
            if 0 <= nx < M and 0 <= ny < N:
                if maps[nx][ny] and not visited[nx][ny]:
                    cnt += 1
                    queue.append([nx,ny])
                    visited[nx][ny] = 1
    return cnt

for _ in range(K):
    y1, x1, y2, x2 = map(int,input().split())
    
    for i in range(x1,x2):
        for j in range(y1,y2):
            maps[i][j] = 0

for i in range(M):
    for j in range(N):
        if maps[i][j] and not visited[i][j]:
            answer += 1
            areas.append(bfs(i,j))

areas.sort()
print(answer)
print(*areas)
