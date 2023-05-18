# 2022.08.15(월)
# B#1655 - < 가운데를 말해요 > - 우선순위 큐
# 문제링크: https://www.acmicpc.net/problem/1655
import heapq
import sys

input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []

for _ in range(N):
    num = int(input())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    
    else:
        heapq.heappush(right_heap, num)
        
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value * -1)

    print(left_heap[0] * -1)