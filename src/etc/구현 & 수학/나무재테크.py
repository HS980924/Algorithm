# 2022.08.15(월)
# <B#.16235> 나무재테크 - 구현 
# 참고링크 : https://www.acmicpc.net/problem/16235

import sys
from collections import deque

N, M, K = map(int,sys.stdin.readline().split())
food = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
land = [[5 for _ in range(N)] for _ in range(N)]
word = [[deque() for _ in range(N) ] for _ in range(N)]

for i in range(M):
    x, y, z = map(int,sys.stdin.readline().split())
    word[x-1][y-1].append(z)
    
year = 1
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

while year <= K:
    # 봄    (성장)
    for i in range(N):
        for j in range(N):
            if word[i][j]:
                cnt = 0
                for k in range(len(word[i][j])):
                    if land[i][j] - word[i][j][k] >= 0:
                        land[i][j] -= word[i][j][k]
                        word[i][j][k] += 1
                    else:
                        cnt += 1
                # 여름 (죽음)
                for k in range(cnt):
                    land[i][j] += word[i][j].pop() // 2
                    
    # 가을 (번식)
    for i in range(N):
        for j in range(N):
            if word[i][j]:
                for tree in word[i][j]:
                    if tree % 5 == 0:
                        for k in range(8):
                            nx, ny = i+dx[k], j+dy[k]
                            if 0 <= nx < N and 0 <= ny < N:
                                word[nx][ny].appendleft(1)
            
                                
            # 겨울 (양분 추가)
            land[i][j] += food[i][j]
            
    year += 1                         

# 결과값
result = 0
for i in range(N):
    for j in range(N):
        if word[i][j]:
            result += len(word[i][j])
            
print(result)