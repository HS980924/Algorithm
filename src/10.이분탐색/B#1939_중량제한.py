# 2022.07.28(목)
# 중량제한 - 이분탐색
# 문제링크: https://www.acmicpc.net/problem/1939

import sys
from collections import deque

N, M = map(int,input().split())
maps = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    maps[a].append((b,c))
    maps[b].append((a,c))
start,end = map(int,input().split())

def bfs(weight):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    while queue:
        y = queue.popleft()
        for x, w in maps[y]:
            if x not in visited and w >= weight:
                visited.add(x)
                queue.append(x)
    
    return True if end in visited else False

_min, _max = 1, 1000000000
result = _min
while _min <= _max:
    mid = (_max + _min)//2
    if bfs(mid):
        result = mid
        _min = mid+1
    else:
        _max = mid-1
print(result)

