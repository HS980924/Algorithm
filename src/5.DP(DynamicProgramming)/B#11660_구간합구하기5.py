# Upload BOJ Silver-1 DP 구간 합 구하기5

# 첫번째 시도에서 시간초과가 발생 -> 입력 하는 과정에서 시간 초과 발생하는 듯
# 핵심 알고리즘은 맞았음

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + maps[i-1][j-1]
            
for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
        
    print(result)
    
    