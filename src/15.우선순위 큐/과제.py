# 2022.08.22(월)
# B#13904 < 과제 > - 우선순위 큐
# 문제링크: https://www.acmicpc.net/problem/13904

import heapq
import sys

N = int(input())
assigns = []
result = []
score = 0
day = 0

for _ in range(N):
    d, w = map(int,sys.stdin.readline().split())
    assigns.append([d,w])
assigns.sort()

for x in assigns:
    if result:
        if x[0] > day:
            heapq.heappush(result,(x[1],x[0]))
            score += x[1]
            day += 1
        else:    
            if result[0][1] < x[1]:
                Min = heapq.heappop(result)
                heapq.heappush(result,(x[1],x[0]))
                score -= Min[0]
                score += x[1]
    else:
        heapq.heappush(result,(x[1],x[0]))
        score += x[1]
        day += 1

print(score)
# 30 50 40 60 5