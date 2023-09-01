# Upload BOJ Gold-4 bipartite Graph 1707번 이분 그래프
# 참고 블로그 : https://didu-story.tistory.com/272
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

    
def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    
    while queue:
        node = queue.popleft()
        
        for i in graph[node]:
            if not visited[i]:
                visited[i] = -visited[node]
                queue.append(i)
            else:
                if visited[i] == visited[node]:
                    return False
    return True


for _ in range(T):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    flag = True
    
    for i in range(E):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for i in range(1,V+1):
        if visited[i] == 0:
            result = bfs(i)
            if not result:
                flag = False
                break
    
    if flag:
        print("YES")
    else:
        print("NO")
