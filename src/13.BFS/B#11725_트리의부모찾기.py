# Upload BOJ Silver-2 BFS 11725번 트리의 부모 찾기
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int,input().split())
    graph[b].append(a)
    graph[a].append(b)

visited = [0]*(N+1)

queue = deque()
queue.append(1)
visited[1] = 1

while queue:
    node = queue.popleft()
    
    for value in graph[node]:
        if not visited[value]:
            visited[value] = node
            queue.append(value)

for value in visited[2:]:
    print(value)

