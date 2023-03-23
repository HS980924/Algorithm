# 참고 링크 : https://hongcoding.tistory.com/18
from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
ways = [[0,1],[1,0],[-1,0],[0,-1]]
visited[0][0][0] += 1

def bfs(x,y,z):
    queue = deque()
    queue.append([x,y,z])

    while queue:
        loc = queue.popleft()
        
        if loc[0] == N-1 and loc[1] == M-1:
            return visited[loc[0]][loc[1]][loc[2]]
        
        for i in range(4):
            nx, ny, nz = ways[i][0] + loc[0], ways[i][1] + loc[1], loc[2]
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 0 and not visited[nx][ny][nz]:
                    visited[nx][ny][nz] = visited[loc[0]][loc[1]][loc[2]] + 1
                    queue.append([nx,ny,nz])
                if maps[nx][ny] and nz == 0:
                    visited[nx][ny][1] = visited[loc[0]][loc[1]][nz] + 1
                    queue.append([nx,ny,1])
    return -1

print(bfs(0,0,0))
