# 2022.08.21(일)
# B#2470 < 두 용액 > - 이분탐색
# 문제링크 : https://www.acmicpc.net/problem/2470

N = int(input())
liquid= list(map(int,input().split()))
liquid.sort()

left = 0
right = N-1

values = [liquid[left],liquid[right]]
SUM = sum(values)


while left < right:
    result = liquid[left] + liquid[right]
    
    if abs(result) < abs(SUM):
        values = [liquid[left],liquid[right]]
        SUM = sum(values)
        if SUM == 0:
            break
    if result < 0:
        left += 1
    else:
        right -= 1

print(*values)