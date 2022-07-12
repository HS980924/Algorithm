# 2022.07.06(수)
# 이동하기 - 다이나믹프로그래밍 (DP)
# 문제 링크 : https://www.acmicpc.net/problem/11048
import sys

N, M = map(int,input().split())
miro = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp[1][1] = miro[0][0]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = miro[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[N][M])
