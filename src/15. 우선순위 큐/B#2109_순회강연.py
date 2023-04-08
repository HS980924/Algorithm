# import sys
# from heapq import heappush, heappop

# N = int(input())
# info = []
# heap = []

# for _ in range(N):
#     info.append(list(map(int,sys.stdin.readline().split())))

# info.sort(key=lambda x : x[1])

# day = 0
# answer = 0

# for p, d in info:
#     if not heap:
#         heappush(heap,(p,d))
#         day += 1
#     else:
#         if heap[0][0] < p:
#             if day < d:
#                 day += 1
#             heappush(heap,(p,d))
#             while len(heap) > day:
#                 heappop(heap)
#         else:
#             if day < d:
#                 heappush(heap,(p,d))
#                 day += 1

# while heap:
#     pay, d = heappop(heap)
#     answer += pay

# print(answer)
# (10, 1) (5, 1) (30,2) (40,2) (20,3) (50,3) (60,3) (70,3)
# 30 + 40 = 70 최대

# 최소힙을 만듦 (p 기준)
# 다음 p값이 heap에 들어있는 p값보다 크다. 그럼 push를 하고 pop을 함
# len(heap) == day 같아야함

# (10,1) (5,2)
import sys
from heapq import heappush, heappop

N = int(input())
info = []
heap = []

for _ in range(N):
    info.append(list(map(int,sys.stdin.readline().split())))

info.sort(key=lambda x : x[1])

for p, d in info:
    heappush(heap,p)
    if len(heap) > d:
        heappop(heap)

print(sum(heap))


