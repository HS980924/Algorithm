from collections import deque

N, L, R = map(int, input().split())
maps = [ list(map(int,input().split())) for _ in range(N)]
ways = [[0,1],[1,0],[-1,0],[0,-1]]
day = 0

def bfs(x,y):
    Union_contries = []
    population = 0
    
    queue = deque()
    queue.append([x,y])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x +ways[i][0], y+ways[i][1]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(maps[x][y] - maps[nx][ny]) <= R:
                    queue.append([nx,ny])
                    visited[nx][ny] = 1
                    population += maps[nx][ny]
                    Union_contries.append([nx,ny])
    
    if Union_contries:
        value = population // len(Union_contries)
        for x, y in Union_contries:
            maps[x][y] = value
        return 1
    
    return 0

while True:
    visited = [ [ 0 for _ in range(N) ] for _ in range(N)]
    check = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                check += bfs(i,j)
    
    if check:
        day += 1
    else:
        break

print(day)