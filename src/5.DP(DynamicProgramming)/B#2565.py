N = int(input())
wire = [list(map(int,input().split())) for _ in range(N)]
wire2 = []
dp = [0]*N

wire.sort()

for i in range(N):
    wire2.append(wire[i][1])

for i in range(N):
    for j in range(i):
        if wire2[i] > wire2[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(N-max(dp))



