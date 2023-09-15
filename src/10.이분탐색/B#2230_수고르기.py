# Upload BOJ Gold-5 BinarySearch & Two Pointer 2230번 수 고르기
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

def bs(arr, N, M):
    answer = arr[-1] - arr[0]

    for i in range(N-1):
        left = i+1
        right = N-1
        
        while left <= right:
            mid = (left+right) // 2
            res = arr[mid] - arr[i]
            if res < M:
                left = mid + 1
            elif res > M:
                answer = min(answer, res)
                right = mid - 1
            else:
                answer = res
                return answer
    return answer

print(bs(arr, N, M))


# def solution(arr, N, M):
#     answer = arr[-1] - arr[0]
    
#     for i in range(N-1):
#         for j in range(i+1,N):
#             res = arr[j] - arr[i]
#             if res > M:
#                 answer = min(answer,res)
#             elif res == M:
#                 answer = res
#                 return answer
            
#     return answer
# print(solution(arr,N,M))
