# Upload BOJ Silver-2 BFS 4963번 섬의 개수
from collections import deque  

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    ways = [[0,1],[1,0],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
    
    while queue:
        x, y = queue.popleft()

        for way in ways:
            nx, ny = x+way[0], y+way[1]
            
            if 0 <= nx < height and 0 <= ny < width:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = 1

while True:
    width, height = map(int,input().split())
    
    if width == 0 or height == 0:
        break
    
    maps = [list(map(int,input().split())) for _ in range(height)]
    visited = [[0 for _ in range(width)] for _ in range(height)]
    cnt = 0
    
    for i in range(height):
        for j in range(width):
            if maps[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)
