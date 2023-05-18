from collections import deque

def solution(maps):
    answer = 0
    queue = deque([])
    n, m = len(maps)-1, len(maps[0])-1
    queue.append([0,0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            
            if 0 <= nx <= n and 0 <= ny <= m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx,ny])
    
    if maps[n][m] == 1:
        answer = -1
    else:
        answer = maps[n][m]
    
    return answer