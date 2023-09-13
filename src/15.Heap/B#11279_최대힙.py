# Upload BOJ Silver-2 Heap 11279번 최대힙
import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(heap,-num)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)