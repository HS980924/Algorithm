import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(input().strip()) for _ in range(N)]

moves = [[0]*M for _ in range(N)]
ways = [[1,0],[0,1],[-1,0],[0,-1]]
queue = deque()
queue.append([0,0])
moves[0][0] = 1

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x+ways[i][0], y+ways[i][1]
        
        if 0 <= nx < N and 0 <= ny < M and int(maps[nx][ny]) and not moves[nx][ny]:
            queue.append([nx,ny])
            moves[nx][ny] = moves[x][y] + 1

print(moves[N-1][M-1])
