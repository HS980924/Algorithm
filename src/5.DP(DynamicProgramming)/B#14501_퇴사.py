# Upload BOJ Silver-3 DP 퇴사
# N = int(input())

# schedule = [list(map(int,input().split())) for _ in range(N)]
# dp = [0]*(N+1)

# for i in range(1,N+1):
#     T, P = schedule[i-1]
#     if T == 1:
#         dp[i] = max(dp[i], dp[i-1]+P)
#     else:
#         if i+T-1 <= N:
#             dp[i+T-1] = max(dp[i-1]+P, dp[i+T-1])
#         dp[i] = max(dp[i-1], dp[i])

# print(dp[-1])


n = int(input())
data = []
dp = [0] * (n + 1)
for i in range(1, n + 1):
    data.append(list(map(int, input().split())))


for i in range(n):
    for j in range(i + data[i][0], n + 1):
        dp[j] = max(dp[j], dp[i] + data[i][1])
    print(dp)

print(dp[-1])