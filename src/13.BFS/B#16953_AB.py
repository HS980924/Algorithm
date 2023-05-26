# Upload BOJ Silver-2 Greedy A -> B
# from collections import deque


# def BFS(a, b):
#     q = deque()
#     q.append(a)
    
#     numbers = set()
#     cnt = 0
    
#     while q:
#         num = q.popleft()
        
#         if num == b:
#             return cnt + 1
#         else:
#             if num < b:
#                 numbers.add(num*2)
#                 numbers.add(int(str(num)+'1'))

#         if not q:
#             for x in numbers:
#                 q.append(x)
#             numbers.clear()
#             cnt += 1

#     return -1
        
# A, B = map(int,input().split())
# print(BFS(A,B))


############################################
from collections import deque
a,b = map(int,input().split())
q = deque()
q.append((a,1))
r = 0

while q:
    n,t = q.popleft()
    if n > b:
        continue
    if n == b:
        print(t)
        break
    q.append((int(str(n)+"1"),t+1))
    q.append((n*2,t+1))
else:
    print(-1)