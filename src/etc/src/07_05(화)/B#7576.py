# 토마토
# BFS, 그래프 탐색, 그래프 이론
# 리스트에서 pop()과 deque에서 popleft()시간 초과 차이가 있음
# 해당 문제 알고리즘은 맞았지만 시간 초과가 계속 났음
# deque와 리스트 시간 복잡도의 문제였음
import sys
from collections import deque

def bfs(maxRow, maxCol):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    global tomoto
    global queue
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < maxRow and 0 <= ny < maxCol and tomoto[nx][ny] == 0:
                tomoto[nx][ny] = tomoto[x][y] + 1
                queue.append((nx,ny))


col, row = map(int,input().split())
tomoto = [list(map(int,sys.stdin.readline().split())) for i in range(row)]
queue = deque([])

for i in range(row):
    for j in range(col):
        if tomoto[i][j] == 1:
            queue.append([i,j])

bfs(row, col)

answer = 0

for x in tomoto:
    if 0 in x:
        answer = 0
        break
    answer = max(max(x),answer)

print(answer-1)
