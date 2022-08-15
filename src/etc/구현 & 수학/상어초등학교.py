# 2022.08.15(월)
# 상어 초등학교 - 구현
# 참고링크 : https://www.acmicpc.net/status?user_id=choihs0924&problem_id=21608&from_mine=1

import sys

N = int(input())
room = [[0 for _ in range(N)] for _ in range(N)]
orders = []
likes = {}
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N**2):
    tmp = list(map(int,sys.stdin.readline().split()))
    orders.append(tmp[0])
    likes[tmp[0]] = tmp[1:]

def checking(num):
    loc = [0,0]
    preBlank = -1
    preCnt = -1
    tmp = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == 0:
                cnt = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if room[nx][ny] in likes[num]:
                            cnt += 1
                        if room[nx][ny] == 0:
                            blank += 1
                if preCnt < cnt:
                    preCnt = cnt
                    preBlank = blank
                    loc[0], loc[1] = i, j
                elif preCnt == cnt:
                    if preBlank < blank:
                        preBlank = blank
                        loc[0], loc[1] = i, j
            else:
                continue
    
    return loc

def scoreSum():
    result = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < N and 0 <= ny < N and room[nx][ny] in likes[room[i][j]]:
                    cnt += 1
            if cnt != 0:
                result += 10**(cnt-1)
    
    return result    

for order in orders:
    loc = checking(order)
    room[loc[0]][loc[1]] = order
    
answer = scoreSum()
print(answer)

