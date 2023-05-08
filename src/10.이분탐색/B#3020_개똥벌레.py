import sys
input = sys.stdin.readline

N, H = map(int, input().split())

up = [0]*(H+1)   # 종유석
down = [0]*(H+1) # 석순

for i in range(N):
    if i % 2 == 0:
        down[int(input())] += 1 # 입력한 높이에서 파괴할 수 있는 석순 갯수
    else:
        up[int(input())] += 1   # 입력한 높이에서 파괴할 수 있는 종유석 갯수

for i in range(H-1,0,-1):
    down[i] += down[i+1]        # 석순 파괴 갯수 누적합 (높이5에서 파괴한 석순은 높이4에서도 파괴할 수 있음)
    up[i] += up[i+1]            # 종류석 파괴 갯수 누적합 (높이5에서 파괴한 종유석은 높이4에서도 파괴할 수 있음)


minCnt = N
rangeCnt = 0
for i in range(1,H+1):
    if down[i] + up[H-i+1] < minCnt:
        minCnt = down[i] + up[H-i+1]
        rangeCnt = 1
    elif down[i] + up[H-i+1] == minCnt:
        rangeCnt += 1

print(minCnt, rangeCnt)


# 참고 링크 : https://hongcoding.tistory.com/6
