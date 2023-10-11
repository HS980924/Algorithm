# Upload BOJ Gold-5 Heap & Dijkstra 5972번 택배 배송
import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2, weight = map(int,input().split())
    graph[v1].append([v2,weight])
    graph[v2].append([v1,weight])
    
def dijkstra(start):
    visited = [INF]*(N+1)
    visited[start] = 0
    heap = []
    heapq.heappush(heap,[start,0])
    
    while heap:
        node, weight = heapq.heappop(heap)
        
        
        for next_node, next_weight in graph[node]:
            total_weight = next_weight + weight
            if visited[next_node] > total_weight:
                heapq.heappush(heap,[next_node,total_weight])
                visited[next_node] = total_weight
        
    return visited[N]

print(dijkstra(1))
