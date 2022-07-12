# 2022.07.06(수)
# 치킨 배달 - 백트래킹 (BackTracking)
# 문제 링크 : https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

N, M = map(int,input().split())
city = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
distance = [[0 for _ in range(N)] for _ in range(N)]
answer = []
homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i,j))
        elif city[i][j] == 2:
            chickens.append((i,j))
            
            
for chichen in combinations(chickens,M):
    result = 0
    for home in homes:
        dis = 99999
        for chi in chichen:
            dis = min(dis,abs(chi[0]-home[0]) + abs(chi[1]-home[1]))
        result += dis
    answer.append(result)

print(min(answer))



# def dfs(distance,index,cnt,m):
#     global chicken, home, answer, city
    
#     if cnt == m:
#         SUM = 0
#         for value in distance:
#             SUM += sum(value)
#         answer.append(SUM)
#         return
    
#     if index >= len(chicken):
#         return
    
#     tmp = copy.deepcopy(distance)
    
#     for i in range(index,len(chicken)):
#         x = chicken[i][0]
#         y = chicken[i][1]
        
#         for nx,ny in home:
#             dis = abs(nx-x) + abs(ny-y)
#             if distance[nx][ny] == 0:
#                 distance[nx][ny] = dis
#             else:
#                 if distance[nx][ny] > dis:
#                     distance[nx][ny] = dis
#         dfs(distance,i+1,cnt+1,m)
#         distance = copy.deepcopy(tmp)
    
#     return

# dfs(distance,0,0,M)
# print(min(answer))

