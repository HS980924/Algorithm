from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
answer = 0

def bfs(i):
    q = deque([i])
    visited[i] = 1
    
    while q:
        v = q.popleft()
        
        for value in graph[v]:
            if not visited[value]:
                q.append(value)
                visited[value] = 1
    
    return 1

for i in range(1,N+1):
    if not visited[i]:
        answer += bfs(i)

print(answer)
