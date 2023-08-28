# Upload BOJ Gold-2 Topology Sort & Heap 1766번 문제집
import sys
import heapq

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
queue = []
answer = []

for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    inDegree[B] += 1

for i in range(1,N+1):
    if inDegree[i] == 0:
        heapq.heappush(queue,i)

while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(queue,i)

print(*answer)