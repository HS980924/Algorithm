# Upload BOJ Silver-3 Deque 1021번 회전하는 큐
from collections import deque

N, M = map(int,input().split())
orders = list(map(int,input().split()))
nums = deque([x for x in range(1,N+1)])
answer = 0

for value in orders:
    idx = nums.index(value)
    while value != nums[0]:
        if idx <= len(nums)/2:
            nums.append(nums.popleft())
        else:
            nums.appendleft(nums.pop())
        answer += 1
    nums.popleft()
    
print(answer)