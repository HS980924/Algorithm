# Upload BOJ Gold-5 이분 탐색 3079번 입국심사
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
times = []

for _ in range(N):
    times.append(int(input()))
times.sort()

left = 1
right = 1000000000000000001
while left <= right:
    mid = (left + right)//2
    cnt = 0
    
    for time in times:
        cnt += mid // time 
        
    if cnt < M:
        left = mid + 1
    else:
        right = mid - 1
        
print(right+1)




# heap 사용 시 시간 초과
# import sys, heapq

# input = sys.stdin.readline

# N, M = map(int,input().split())
# heap = []

# for _ in range(N):
#     time = int(input())
#     heapq.heappush(heap,[time,time])

# time = 0
# cnt = 0
# while cnt < M:
#     while heap[0][0] <= time:
#         times = heapq.heappop(heap)
#         cnt += 1
#         outTime = time+times[1]
#         heapq.heappush(heap,[outTime, times[1]])
#     time += 1

# print(time-1)
