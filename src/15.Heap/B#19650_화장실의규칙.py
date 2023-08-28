import sys
import heapq
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
queue = [deque() for _ in range(M)]
heap = []
order = 0

for i in range(N):
    info = list(map(int, input().split()))
    info[0], info[1] = info[0]*-1, info[1]*-1
    info += [(i%M)+1]
    if i == K:
        info += [True]
    else:
        info += [False]
    queue[i%M].append(info)

for i in range(M):
    if queue[i]:
        heapq.heappush(heap,queue[i].popleft())

while heap:
    employee = heapq.heappop(heap)
    if employee[-1]:
        break
    order += 1
    if queue[employee[-2]-1]:
        tmp = queue[employee[-2]-1].popleft()
        heapq.heappush(heap,tmp)

print(order)