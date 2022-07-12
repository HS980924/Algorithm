N, K = map(int,input().split())
pd = [[0,0]]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N):
    W, V = map(int,input().split())
    pd.append([W,V])

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= pd[i][0]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-pd[i][0]]+pd[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])