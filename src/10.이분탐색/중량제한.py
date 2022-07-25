# 2022.07.18(월)
# 중량제한 - 이분탐색
# 문제링크: https://www.acmicpc.net/problem/1939

import sys

N, M = map(int,input().split())
brige = [[0 for _ in range(M+1)] for _ in range(M+1)]
weight = []

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    if brige[a][b] < c:
        brige[a][b] = c
        brige[b][a] = c

island = list(map(int,sys.stdin.readline().split()))


print(brige[1:])
print(island)
