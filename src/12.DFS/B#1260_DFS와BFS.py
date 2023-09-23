# Upload BOJ Silver-2 DFS & BFS 1260번 DFS와BFS
from collections import deque
N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
answers = [[]]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(v):
    answers[0].append(v)
    visited[v] = True
    graph[v].sort()
    
    for node in graph[v]:
        if not visited[node]:
            DFS(node)

def BFS(v):
    queue = deque([])
    queue.append(v)
    visited[v] = True
    
    tmp = []
    while queue:
        v = queue.popleft()
        tmp.append(v)
        
        graph[v].sort()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                
    answers.append(tmp)
    

for i in range(2):
    visited = [False]*(N+1)
    if i == 0:
        DFS(V)
    else:
        BFS(V)

for answer in answers:
    print(*answer)