# 2022.07.08(금)
# 욕심쟁이 판다 - DP & DFS
# 문제 링크 : https://www.acmicpc.net/problem/1937
# 관련 레퍼런스 : https://kyun2da.github.io/2021/04/04/panda/
# 개념 영상 : https://www.youtube.com/user/damazzang/videos
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y    
        if 0 <= nx < N and 0 <= ny < N and forest[x][y] < forest[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
            
    return dp[x][y]

N = int(input())
forest = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer,dfs(i,j))

print(answer)



