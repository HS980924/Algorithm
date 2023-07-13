N, K = map(int,input().split())
dp = [K+1 for _ in range(K+1)]
dp[0] = 0
coin = set()

for _ in range(N):
    coin.add(int(input()))

coins = list(coin)
coins.sort()

for i in range(1,K+1):
    for x in coins:
        if i-x >= 0:
            dp[i] = min(dp[i-x]+1,dp[i])

if dp[K] == K+1:
    print(-1)
else:
    print(dp[K])