# Upload BOJ Gold-4 DP 타일채우기 (3xN)
N = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 1

for i in range(2,N+1):
    for j in range(i-2,-1,-2):
        if j == i-2:
            dp[i] += dp[j]*3
        else:
            dp[i] += dp[j]*2
print(dp[N])