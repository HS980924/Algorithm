import sys
from heapq import heappush, heappop
N = int(input())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heappush(heap,(abs(num),num))
    else:
        if heap:
            data = heappop(heap)
            print(data[1])
        else:
            print(0)