# Upload BOJ Silver-3 Brute Force & Backtracking 18429번 근손실 
# 하루가 지날때 마다 중량 K만큼 감소
# K=4 3일이 지나면 12중량 감소
# 조합문제?

from itertools import permutations

N, K = map(int,input().split())
kit = list(map(int,input().split()))
orders = permutations(range(0,len(kit)),len(kit))

cnt = 0
for order in orders:
    answer = 500
    check = True
    for idx in order:
        answer += kit[idx] - K
        if answer < 500:
            check = False
            break
    if check:
        cnt += 1
print(cnt)