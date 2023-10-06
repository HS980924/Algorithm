# Upload BOJ Silver-1 BFS 7562번 나이트의이동
from collections import deque

def bfs(x, y, lx, ly, I):
    queue = deque()
    visited = [[0 for _ in range(I)] for _ in range(I)]
    queue.append([x,y,0])
    visited[x][y] = 1
    
    ways = [[-2,-1],[-2,1],[-1,2],[1,2],[2,-1],[2,1],[-1,-2],[1,-2]]
    
    while queue:
        x, y, move = queue.popleft()
        
        if x == lx and y == ly:
            return move
        
        for way in ways:
            nx, ny = x+way[0], y+way[1]
            
            if 0 <= nx < I and 0 <= ny < I:
                if not visited[nx][ny]:
                    queue.append([nx,ny,move+1])
                    visited[nx][ny] = 1

T = int(input())

for _ in range(T):
    I = int(input())
    
    x, y = map(int,input().split())
    lx, ly = map(int,input().split())
    
    print(bfs(x,y,lx,ly,I))
