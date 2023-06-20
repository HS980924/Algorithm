# Upload Silver-3 BFS 바이러스

from collections import deque

N = int(input())
pair = int(input())
visited = [0]*(N+1)
queue = deque()
graph = [[] for _ in range(N+1)]
answer = 0

for _ in range(pair):
    x, y = map(int,input().split())
    graph[x] += [y]
    graph[y] += [x]
    
visited[1] = 1
queue.append(1)

while queue:
    computerNum = queue.popleft()
    for x in graph[computerNum]:
        if not visited[x]:
            queue.append(x)
            visited[x] = 1
            answer += 1

print(answer)