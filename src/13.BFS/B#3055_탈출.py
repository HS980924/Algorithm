# Upload BOJ Gold-4 BFS 탈출
from collections import deque

R, C = map(int,input().split())
maps = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
ways = [[0,1],[0,-1],[1,0],[-1,0]]

waters = []
biber = []

for i in range(R):
    for j in range(C):
        if maps[i][j] == "*":
            waters.append([i,j])
        elif maps[i][j] == "S":
            maps[i][j] = '.'
            biber.append([i,j])

def BFS(waters, biber):
    waters_q = deque()
    biber_q = deque()
    
    for value in waters:
        waters_q.append(value)
        
    for value in biber:
        biber_q.append(value)
        
    while True:
        if not biber_q:
            break
        water_list = []
        biber_list = []
        
        while waters_q:
            x, y = waters_q.popleft()
            for i in range(4):
                nx, ny = x+ways[i][0], y+ways[i][1]
                
                if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] == '.':
                    maps[nx][ny] = '*'
                    water_list.append([nx,ny])
        
        while biber_q:
            x, y = biber_q.popleft()
            for i in range(4):
                nx, ny = x+ways[i][0], y+ways[i][1]
                
                if 0 <= nx < R and 0 <= ny < C:
                    if not visited[nx][ny] and (maps[nx][ny] == '.' or maps[nx][ny] == 'D'):
                        visited[nx][ny] = visited[x][y] + 1
                        biber_list.append([nx,ny])
        
        for x in water_list:
            waters_q.append(x)
            
        for x in biber_list:
            biber_q.append(x)
    
    for i in range(R):
        for j in range(C):
            if maps[i][j] == "D":
                if visited[i][j]:
                    return visited[i][j]
                else:
                    return "KAKTUS"
                
print(BFS(waters,biber))