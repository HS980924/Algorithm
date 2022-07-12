# def solution(n):
#     dp = [0 for i in range(n+1)]
#     dp[1] = 1
#     for i in range(2,n+1):
#         if i % 2 == 0:
#             dp[i] = min(i, dp[i-1]+1, dp[i//2])
#         else:
#             dp[i] = min(i, dp[i-1]+1, dp[(i-1)//2]+1)
    
#     print(dp)
#     return dp[n]

# n = 5000
# print(solution(n))

# def solution(n):
#     ans = 0
    
#     while n > 0:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             ans += 1
#             n = (n-1)//2
            
#     return ans

# n = 5000
# print(solution(n))

# 해당 값이 짝수일 경우 //2 에서의 횟수랑 같음  
# 해당 값이 홀수일 경우 +1 의 횟수랑 같음
# 이진값으로 변환하여 1의 갯수만 세는것이 홀수일때 움직인 거리와 같음

def solution(n):
    return bin(n).count('1') 

n = 5000
print(solution(n))
