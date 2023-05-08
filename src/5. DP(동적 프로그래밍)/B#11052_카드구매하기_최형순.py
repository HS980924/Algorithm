# 내 풀이
N = int(input())
cards = list(map(int, input().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
    tmp = []
    for j in range(N//2+1):
        tmp.append(dp[i-j]+dp[j])
    tmp.append(cards[i-1])
    dp[i] = max(tmp)

print(dp[N])

# 다른 사람 풀이
import sys
input=sys.stdin.readline
print=sys.stdout.write
N = int(input())
dp = [0]*(N+1)

for i,v in enumerate(map(int, input().split()), 1):
    dp[i] = v
    dp[i] = max([dp[j]+dp[i-j] for j in range(0,i//2+1)])

print(str(dp[-1]))