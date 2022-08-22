# 2022.08.22(월)
# B#11000 < 강의실 배정 > - 우선순위 큐
# 문제링크: https://www.acmicpc.net/problem/11000

import sys, heapq

N = int(input())
times = []
end = []
cnt = 0

for _ in range(N):
    S, T = map(int,sys.stdin.readline().split())
    heapq.heappush(times,(S, [S, T]))

while times:
    result = heapq.heappop(times)
    if end:
        if end[0] <= result[1][0]:
            heapq.heappop(end)
            heapq.heappush(end,result[1][1])
        else:
            heapq.heappush(end,result[1][1])
            cnt += 1
    else:
        heapq.heappush(end,result[1][1])
        cnt += 1

print(cnt)