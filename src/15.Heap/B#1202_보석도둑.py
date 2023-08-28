# Upload BOJ Gold-2 Greedy & Heap 1202번 보석도둑
# 참고 블로그 : https://bio-info.tistory.com/195
import heapq, sys
input = sys.stdin.readline

N, K = map(int,input().split())
jewel = []
bags = []

for _ in range(N):
    weight, price = map(int,input().split())
    heapq.heappush(jewel,[weight,price])

for _ in range(K):
    bags.append(int(input()))
    
bags.sort()
answer = 0
tmp = []

for bag in bags:
    while jewel and jewel[0][0] <= bag:
        heapq.heappush(tmp,-jewel[0][1])
        heapq.heappop(jewel)
    if tmp:
        answer -= heapq.heappop(tmp)
        
print(answer)
