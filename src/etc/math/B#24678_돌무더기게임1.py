# Upload BOJ Gold-3 math 24678번 돌무더기게임1
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    odd = 0
    even = 0
    stones = list(map(int,input().split()))
    
    for stone in stones:
        if stone % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == 3 or even == 2:
        print('R')
    else:
        print('B')
# 1 3 2

# 1 -> 4 1
# 1 -> 3 1
# 1 -> 2 1
# 1 -> 1 1
# 1 -> 0 0 
    
# import sys
# input = sys.stdin.readline

# T = int(input())
# # order 1 : R
# # order -1 : B

# for _ in range(T):
#     stones = list(map(int,input().split()))
#     stones.sort()
#     order = 1
#     while stones[0] + stones[1] != 0:
#         cnt = 0
#         tmp = []
#         for i in range(3):
#             if stones[i] != 0:
#                 cnt += 1
#                 stones[i] -= 1
#                 tmp.append(i)
#             if cnt == 2:
#                 for j in range(3):
#                     if not j in tmp:
#                         stones[j] += 1
#                 break
#         order = order * (-1)
#         stones.sort()
        
#     if order == 1:
#         print("R")
#     else:
#         print("B")      

    
# 돌무더기 중 가장 적게 들어 있는 돌무더기 2개 택
#   단, 돌 무더기가 0일 경우 패스
# 택한 돌무더기에서 하나씩 Get
# 가장 많이 쌓인 돌무더기에 하나를 push
# 순서 교체
# 돌무더기 두개가 0일 경우 Game Over

# 2개의 돌 무더기 택하는 알고리즘
# 선택되지 않은 돌 무더기 확인
# 각 돌 무더기의 갯수가 최대 10^9 즉, 하나씩 빼고 더하는건 너무 비효율적
# 총 시행 횟수를 알면 정답을 알 수 있음
# 그렇다면 총 시행 횟수를 어떻게 구할 것 인가?
# -1, -1, +1 이렇게 진행되는데 이 횟수를 전체 돌 무더기 갯수에서 나누면 될까?
# 막대기 자르는 것 처럼 진행?

# 1 3 2   0
# 0 2 3   1
# 1 1 2   2
# 0 0 3   3

# 2 0 1   3
# 1 1 0   4
# 0 0 1   5

# 1 3 2     0
# 0 4 1     1
# 1 3 0     2
# 0 2 1     3
# 1 1 0     4
# 0 0 1     5


# 규칙 찾기 -> 중요  규칙 -> 
# 