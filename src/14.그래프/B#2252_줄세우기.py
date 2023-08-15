# Upload BOJ Gold-3 Topological Sorting & Graph 2252번 줄세우기
# https://velog.io/@kimdukbae/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC-Topological-Sorting
# 참고 링크
from collections import deque

N, M = map(int,input().split())
graph = [ [] for _ in range(N+1)]
indegree = [0]*(N+1)
result = []

for i in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    indegree[B] += 1
    
def topology_sort():
    q = deque()
    
    for i in range(1,N+1):
        if not indegree[i]:
            q.append(i)
    
    while q:
        num = q.popleft()
        result.append(num)
        
        for value in graph[num]:
            indegree[value] -= 1
            if not indegree[value]:
                q.append(value)

topology_sort()
print(*result)
