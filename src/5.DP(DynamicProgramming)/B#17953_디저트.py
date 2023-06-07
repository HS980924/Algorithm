# Upload BOJ Gold-5 DP 디저트
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
info = [list(map(int,input().split())) for _ in range(M)]
dp = [ [0 for _ in range(N)] for _ in range(M)]

for i in range(M):
    dp[i][0] = info[i][0]

for day in range(1,N):
    for dessert in range(M):
        for i in range(M):
            if i == dessert:
                dp[dessert][day] = max(dp[dessert][day], info[dessert][day]//2 + dp[i][day-1])
            else:
                dp[dessert][day] = max(dp[dessert][day], info[dessert][day] + dp[i][day-1])

result = 0
for i in range(M):
    result = max(result,dp[i][-1])

print(result)