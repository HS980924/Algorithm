N = int(input())
Num = list(map(int,input().split()))
Num_len = len(Num)
dp = [-1000 for _ in range(Num_len)]

for i in range(Num_len):
    dp[i] = max(dp[i-1] + Num[i],Num[i])

print(max(dp))
    