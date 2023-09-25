# Upload BOJ Silver-1 BFS 2468번 안전영역
from collections import deque

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
maxHeight = 0
answer = 0

def BFS(height, cnt, x, y):
    queue = deque()
    queue.append([x,y])
    ways = [[0,1],[1,0],[-1,0],[0,-1]]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x+ways[i][0], y+ways[i][1]

            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] > height and not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = cnt 


for row in maps:
    maxHeight = max(max(row), maxHeight)

for height in range(maxHeight+1):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if maps[x][y] > height and not visited[x][y]:
                cnt += 1
                BFS(height, cnt, x, y)

    answer = max(cnt,answer)

print(answer)