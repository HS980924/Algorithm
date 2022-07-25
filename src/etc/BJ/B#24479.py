# 알고리즘 수업 - 깊이 우선 탐색 1
# 2022.06.27(월)
import sys

edge = []
V, E, R = map(int,input().split())

for i in range(E):
    start,end = map(int,sys.stdin.readline().split())
    edge.append((start,end))

def dfs(v,e,r):
    pass
