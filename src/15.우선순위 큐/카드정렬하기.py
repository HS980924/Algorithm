# 2022.08.22(월)
# B#1715 < 카드 정렬하기 > - 우선순위 큐
# 문제링크: https://www.acmicpc.net/problem/1715

import sys, heapq

N = int(input())
cards = [int(sys.stdin.readline()) for _ in range(N)]
result = 0
heapq.heapify(cards)

while len(cards) > 1:    
    value1 = heapq.heappop(cards)
    value2 = heapq.heappop(cards)
    valueSum = value1 + value2
    result += valueSum
    heapq.heappush(cards,valueSum)

print(result)
