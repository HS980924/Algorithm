'''
N = int(input())
Wine = [0]
dp = [0]
for i in range(N):
    Wine.append(int(input()))

dp.append(Wine[1])
if(N>1):
    dp.append(Wine[1] + Wine[2])
for i in range(3,N+1):
        dp.append(max(dp[i-1], dp[i-2] + Wine[i],dp[i-3] + Wine[i-1] + Wine[i]))

print(dp[N])
'''

N = int(input())
Wine = [0]
dp = [0]*(N+1)
for i in range(N):
    Wine.append(int(input()))

dp[1] = Wine[1]
if(N > 1):
    dp[2] = Wine[1] + Wine[2]

for i in range(3,N+1):
    dp[i] = max(dp[i-3] + Wine[i-1] + Wine[i], dp[i-2] + Wine[i], dp[i-1])

print(dp[N])

















