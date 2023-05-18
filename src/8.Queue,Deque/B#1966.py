# 2022.03.10
# 프린터 큐 - Queue 문제
# 참고 링크: https://www.acmicpc.net/problem/1966

Test_Case = int(input())

for i in range(Test_Case):
    N, M = map(int,input().split())
    Queue = list(map(int,input().split()))
    check = [True]*N
    check[M] = False
    cnt = 1
    
    while check[0] or max(Queue) != Queue[0]:
        MAX = max(Queue)
        if MAX != Queue[0]:
            Queue.append(Queue[0])
            Queue.pop(0)
            check.append(check[0])
            check.pop(0)
        else:
            Queue.pop(0)
            check.pop(0)
            cnt += 1

    print(cnt)

########################다른 사람 풀이##################################
# import sys


# t = int(sys.stdin.readline())

# for _ in range(t):
#     N, M = map(int, sys.stdin.readline().split())
#     lst = list(map(int, sys.stdin.readline().split()))
#     target = lst[M]
#     cnt = 0
#     location = M
    
#     while lst:
#         high = max(lst)
#         if lst[0] < high:
#             if location == 0:
#                 low = lst.pop(0)
#                 lst.append(low)
#                 location = len(lst) - 1
#             else:
#                 low = lst.pop(0)
#                 lst.append(low)
#                 location -= 1
                
#         else:
#             done = lst.pop(0)
#             cnt += 1
#             if done == target and location == 0:
#                 print(cnt)
#                 break
#             else:
#                 location -= 1