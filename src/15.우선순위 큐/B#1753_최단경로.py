# Upload BOJ Gold-4 Graph 최단경로
# from collections import deque
# import sys
# input = sys.stdin.readline

# V, E = map(int,input().split())
# start = int(input())
# graph = [[] for _ in range(V+1)]
# visited = [0 for _ in range(V+1)]
# distance = [0 for _ in range(V+1)]

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u].append([v,w])
    
# def bfs():
#     visited[start] = 1
#     q = deque(graph[start])
    
#     for v, w in graph[start]:
#         distance[v] += w
#         visited[v] = 1
    
#     while q:
#         v = q.popleft()[0]
        
#         for v2, w2 in graph[v]:
#             if not visited[v2]:
#                 distance[v2] += distance[v] + w2
#                 visited[v2] = 1
#                 for g in graph[v2]:
#                     q.append(g)
#             if visited[v2] and distance[v2] > distance[v] + w2:
#                 distance[v2] = distance[u] + w2
# bfs()

# for i in range(1,V+1):
#     if i == start:
#         print(0)
#     else:
#         if distance[i] == 0:
#             print("INF")
#         else:
#             print(distance[i])
            
            
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
#시작점 K
K = int(input())
#가중치 테이블 dp
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    #힙에 원소가 없을 때 까지 반복.
    while heap:
        wei, now = heapq.heappop(heap)

        #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치(next_wei)
            next_wei = w + wei
            #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
            if next_wei < dp[next_node]:
                #계산했던 next_wei를 가중치 테이블에 업데이트.
                dp[next_node] = next_wei
                #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
                heapq.heappush(heap,(next_wei,next_node))

#초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    #(가중치, 목적지 노드) 형태로 저장
    graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])