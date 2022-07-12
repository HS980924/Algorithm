N = int(input())

p = []
dp = []

for i in range(N):
    p.append(list(map(int,input().split())))

dp = p
for i in range(1,N):
    for j in range(3):
        if(j == 0):
            dp[i][j] = min(dp[i-1][j+1], dp[i-1][j+2]) + p[i][j]
        elif(j == 1):
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1]) + p[i][j]
        else:
            dp[i][j] = min(dp[i-1][j-2], dp[i-1][j-1]) + p[i][j]

print(min(dp[N-1]))