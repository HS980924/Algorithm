# Upload BOJ Gold-5 DP 동전1

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0]*(K+1)
dp[0] = 1

coins.sort()

for coin in coins:
    for i in range(coin, K+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[K])