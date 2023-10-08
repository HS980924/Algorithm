# Upload BOJ Gold-4 DP & Floyd-Warshall 11404번 플로이드
# 플로이드-워셜 알고리즘 문제
# 내 생각 알고리즘
# 1. 하나의 도시를 선택하여 해당 도시에서 모든 도시를 갈 때, 최소 가중치 값을 기록
# 2. 모든 도시를 위의 과정을 반복하여 최소 가중치를 값을 기록
# 2-1. 이떄, 앞에서 계산했던 값을 그대로 사용하는 DP 방식 채택하여 계산 시간 줄이기

# 시작 도시와 도착 도시가 같은 경우가 없기 때문 dp[city][city] = 0으로 초기화

# from collections import deque

# N = int(input())
# M = int(input())

# graph = [[] for _ in range(N+1)]
# answer = [[0 for _ in range(N+1)] for _ in range(N+1)]

# for _ in range(M):
#     city1, city2, weigth = map(int,input().split())
#     graph[city1].append([city2,weigth])

# def floyd(start , end):
#     visited = [100001]*(N+1)
#     visited[start] = 0
#     queue = deque()
#     queue.append([start,0])
    
#     while queue:
#         city, weight = queue.popleft();
        
#         for next_city, weight2 in graph[city]:
#             if visited[next_city] > weight2+weight:
#                 visited[next_city] = weight2+weight
#                 queue.append([next_city, weight2+weight])
    
#     if visited[end] == 100001:
#         return 0
#     return visited[end]

# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i == j:
#             continue
#         answer[i][j] = floyd(i,j)

# for value in answer[1:]:
#     print(*value[1:])
# 시간 초과
    

import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0

for _ in range(M):
    city1, city2, weigth = map(int,input().split())
    graph[city1][city2] = min(graph[city1][city2],weigth)
    # 노선이 하나가 아닐 수 있기에 최소 값 넣기
    
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for arr in graph[1:]:
    for value in arr[1:]:
        if value == INF:
            print(0, end=' ')
        else:
            print(value, end=' ')
    print()