# Upload BOJ Gold-4 Spanning tree 1197번 최소 스패닝 트리

# Prim 알고리즘 사용할 예정(알고리즘)
# 준비 : heap 자료구조를 사용
# 1. 시작 정점을 선택 한 후, 해당 정점에 인접한 간선들을 최소 heap에 넣음
# 2. heap에서 가장 작은 간선을 pop한 뒤 사이클이 형성되는지 체크
# 2-1. 사이클이 형성되지 않을 경우 해당 간선을 연결
# 2-2. 사이클이 형성될 경우 heap에서 다음으로 작은 간선을 pop
# 3. N개의 정점이 연결될 떄 까지 위의 과정을 반복

# 여기서 문제
# 1. 사이클 체크 하는 방법? 
#   -> visited 리스트를 만들어 체크하면 될듯?
# 2. N개의 정점 모두가 연결됐는지 체크 하는 방법? 
#   -> 위의 알고리즘에서 반복된 횟수를 체크
import heapq

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
visited = [0]*(V+1)

for _ in range(E):
    v1, v2, weight = map(int,input().split())
    graph[v1].append([weight,v2])
    graph[v2].append([weight,v1])

def PrimMTS(node):
    heap = []
    total_weight = 0
    visited[node] = 1
    cnt = 0
    
    for info in graph[node]:
        heapq.heappush(heap,info)
    
    while cnt < V:
        while heap:
            weight, vertex = heapq.heappop(heap)
            if not visited[vertex]:
                total_weight += weight
                visited[vertex] = 1
                for info in graph[vertex]:
                    heapq.heappush(heap,info)
                break
        cnt += 1
    
    return total_weight

print(PrimMTS(1))


