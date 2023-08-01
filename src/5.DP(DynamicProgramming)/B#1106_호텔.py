# Upload BOJ - Gold5 DP 1106번 호텔
# 홍보 할 수 있는 도시가 주어짐
# 각 도시별로 홍보하는데 드는 비용과 그 때 몇명의 호텔 고객이 늘어나는지 정보
# 각 도시에는 무한 명의 잠재적인 고객
# 적어도 C명을 늘리기 위해 형택이가 투자해야 하는 돈의 최솟값

C, N = map(int,input().split())
cityInfo = [list(map(int,input().split())) for _ in range(N)]
cityInfo.sort()
dp = [1000000]*(C+1)
dp[0] = 0
# city[0] = 비용
# city[1] = 고객

for i in range(1,C+1):
    for j in range(N):
        cost, person = cityInfo[j]
        if i - person >= 0:
            dp[i] = min(dp[i-person] + cost, dp[i])
        else:
            if j == 0:
                dp[i] = cost
print(dp[C])