# 2022.07.13(수)
# 내리막길 - DFS 문제
# 참고링크:https://www.acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(10**6)

M, N = map(int,input().split())
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y+dy[i]
        if 0 <= nx < M and 0 <= ny < N and maps[x][y] > maps[nx][ny]:
            cnt += dfs(nx,ny)
    
    dp[x][y] = cnt
    return dp[x][y]


print(dfs(0,0))