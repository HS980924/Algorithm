from collections import deque
import sys

input = sys.stdin.readline
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def BFS(z,x,y):
    global time
    q.append([z,x,y])
    time[z][x][y] = 1
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if building[nz][nx][ny] == 'E':
                    print("Escaped in " + str(time[z][x][y]) + " minute(s).")
                    return
                if building[nz][nx][ny] == '.' and time[nz][nx][ny] == 0:
                    time[nz][nx][ny] = time[z][x][y] + 1
                    q.append([nz,nx,ny])
    print("Trapped!")

while True:
    L, R, C = map(int, input().split())
    if L + R + C == 0:
        break
    else:
        building = [[[]*C for _ in range(R)] for _ in range(L)]
        time = [[[0]*C for _ in range(R)] for _ in range(L)]
        q = deque()
        for i in range(L):
            building[i] = [list(map(str, input().strip())) for _ in range(R)]
            input()
        
        for i in range(L):
            for j in range(R):
                for k in range(C):
                    if building[i][j][k] == "S":
                        BFS(i,j,k)
        
# 참고 링크 < https://chldkato.tistory.com/41 >      