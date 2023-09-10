# Upload BOJ Silver-4 deque & list 1158번 요세푸스 문제
from collections import deque

N, K = map(int,input().split())
arr = [x+1 for x in range(N)]
queue = deque(arr)

print("<",end="")
while len(queue) > 1:
    for i in range(K-1):
        value = queue.popleft()
        queue.append(value)
    print(queue.popleft(),end="")
    print(",",end=" ")
print(queue.popleft(),end="")
print(">",end="")



# N, K = map(int,input().split())
# arr = [x+1 for x in range(N)]
# idx = 0
# print("<",end="")
# while arr:
#     idx = (idx + K - 1) % len(arr)
#     print(arr.pop(idx),end="")
#     if arr:
#         print(",",end=" ")
# print(">",end="")
