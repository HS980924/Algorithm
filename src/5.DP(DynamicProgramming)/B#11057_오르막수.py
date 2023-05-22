# Upload BOJ Silver-1 DP 오르막수

N = int(input())
dp = [[0]*10 for _ in range(N+1)]

for i in range(10):
    dp[1][i] += dp[1][i-1] + 1


for i in range(2,N+1):
    for j in range(10):
        dp[i][j] += dp[i][j-1] + dp[i-1][j]
        dp[i][j] %= 10007

print(dp[N][-1])