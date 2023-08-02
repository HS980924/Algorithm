# Upload BOJ Gold-2 BFS & Union Find 1765번 닭싸움 팀 정하기
# 닭싸움의 팀을 정하는 원칙
#   1. 내 친구의 친구는 내 친구이다.  < 나 - 친구 - (친구)친구 > 
#   2. 내 원수의 원수도 내 친구이다.  < 나 - 원수 - (원수)친구 >
# 같은 팀에 속해 있는 사람들끼리는 전부 친구여야 함
# 
# F인 경우 p와 q가 친구
# E인 경우 p와 q가 원수인 경우   

from collections import deque

N = int(input()) # 학수의 수 (1 ~ N까지의 번호)
m = int(input()) # 학생간의 관계 수

graph = [[] for _ in range(N+1)]
friend = []
visited = [0]*(N+1)

for _ in range(m):
    relation = list(map(str,input().split()))
    graph[int(relation[1])].append([relation[0],int(relation[2])])
    graph[int(relation[2])].append([relation[0],int(relation[1])])

def bfs(student):
    q = deque()
    
    for relation in graph[student]:
        q.append(relation)
    
    checkVisited = [0]*(N+1)  
    checkVisited[student] = 1 
    
    visited[student] = 1
    
    tmp = [student]
    
    while q:
        relation, idx = q.popleft()
        if relation == 'F' and not checkVisited[idx]:
            for value in graph[idx]:
                q.append(value)
                tmp.append(idx)
            visited[idx] = 1
            checkVisited[idx] = 1
        else:
            if not checkVisited[idx]:
                checkVisited[idx]= 1
                for value in graph[idx]:
                    if value[0] == 'E' and not checkVisited[value[1]]:
                        visited[value[1]] = 1
                        checkVisited[value[1]] = 1
                        tmp.append(value[1])
                        for value2 in graph[value[1]]:
                            q.append(value2)
                        
    return tmp


for i in range(1,N+1):
    if not visited[i]:
        friend.append(bfs(i))

print(len(friend))





