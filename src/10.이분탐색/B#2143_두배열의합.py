# 2022.07.28(목)
# 두배열의합 - >>
# 문제링크 : https://www.acmicpc.net/problem/2143
# 참고링크 : https://velog.io/@nyanyanyong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98python%EB%B0%B1%EC%A4%80-2143%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9
# 참고링크 : https://my-coding-notes.tistory.com/303

import sys
from collections import defaultdict

T = int(input())
N = int(input())
A = list(map(int,sys.stdin.readline().split()))
M = int(input())
B = list(map(int,sys.stdin.readline().split()))

dictA = defaultdict(int)

for i in range(N):
    for j in range(i,N):
        dictA[sum(A[i:j+1])] += 1

answer = 0
for i in range(M):
    for j in range(i,M):
        answer += dictA[T-sum(B[i:j+1])]

print(answer)


#############################

# import sys
# from bisect import bisect_left, bisect_right

# T = int(input())
# N = int(input())
# A = list(map(int,sys.stdin.readline().split()))
# M = int(input())
# B = list(map(int,sys.stdin.readline().split()))

# A_list = []
# for i in range(N):
#     tmp = 0
#     for j in range(i,N):
#         tmp += A[j]
#         A_list.append(tmp)

# B_list = []
# for i in range(M):
#     tmp = 0
#     for j in range(i,M):
#         tmp += B[j]
#         B_list.append(tmp)
        
# B_list.sort()

# answer = 0
# for value in A_list:
#     diff = T-value
#     idx = bisect_left(B_list,diff)
#     if idx >= len(B_list):
#         continue
#     else:
#         idx_end = bisect_right(B_list,diff)
#         if B_list[idx] == diff:
#             answer += idx_end - idx

# print(answer)