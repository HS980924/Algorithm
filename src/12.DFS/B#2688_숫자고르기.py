# Upload BOJ Gold-5 2688번 숫자고르기
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(v,visited):
    visited.add(v)
    checked[v] = 1
    
    for u in graph[v]:
        if u not in visited:
            dfs(u,visited.copy())
        else:
            result.extend(list(visited))
            return

N = int(input())
graph = [[] for _ in range(N+1)]
checked = [0]*(N+1)
result = []

for i in range(1,N+1):
    v = int(input())
    graph[v].append(i)

for i in range(1,N+1):
    if not checked[i]:
        dfs(i,set([]))


result.sort()
print(len(result))
for value in result:
    print(value)