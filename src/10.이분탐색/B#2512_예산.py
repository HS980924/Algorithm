# Upload BOJ Silver-2 BinarySearch 2512번 예산

# 국가의 역할 중 하나는 여러 지방에 국가의 예산을 분배하는 것
# 국가 예산의 총액은 미리 정해져 있다.
# 다음과 같은 방법으로 배정
# 1. 모든 요청이 배정될 수 있는 경우, 요청한 금액을 그대로 배정
# 2. 모든 요청이 배정될 수 없는 경우, 특정한 정수 상한액을 계산하여 그 이상인 
#    예산 요청에는 모두 상한액을 배정, 상한액 이하의 예산 요청에 대해서는 요청한 금액 그대로 배정

N = int(input())
money = list(map(int,input().split()))
M = int(input())

start = 1
end = max(money)

while start <= end:
    mid = (start+end) // 2
    
    budget = 0
    for value in money:
        budget += min(value, mid)

    if budget <= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
