# Upload BOJ Silver-1 Heap 15903번 카드합체놀이
import heapq

N, M = map(int,input().split())
cards = list(map(int,input().split()))
heap = []

for card in cards:
    heapq.heappush(heap,card)

for i in range(M):
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    heapq.heappush(heap,num1+num2)
    heapq.heappush(heap,num1+num2)

print(sum(heap))