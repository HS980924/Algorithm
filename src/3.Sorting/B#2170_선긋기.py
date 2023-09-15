# Upload BOJ Gold-5 Sort & Math 2170번 선긋기
import sys
input = sys.stdin.readline

N = int(input())
pos_arr = []

for _ in range(N):
    x, y = map(int,input().split())
    pos_arr.append([x,y])

pos_arr.sort()

start = pos_arr[0][0]
end = pos_arr[0][1]
length = 0

for pos in pos_arr[1:]:
    if start <= pos[0] and pos[0] <= end:
        start = min(pos[0],start)
        end = max(pos[1],end)
    else:
        length += (end - start)
        start, end = pos[0], pos[1]
length += (end - start)
print(length)