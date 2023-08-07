# Upload BOJ Silver-2 DP 1699번 제곱수의 합
# import math
# N = int(input())
# dp = [100001]*(N+1)
# dp[1] = 1

# for i in range(2,N+1):
#     num = math.floor((i**0.5))
#     if i == num*num:
#         dp[i] = 1
#     else:
#         for j in range(num//2,num+1):
#             dp[i] = min(dp[j**2] + dp[i-j**2], dp[i])
# print(dp[N])


N = int(input())
dp = [100001]*(N+1)
dp[1] = 1

for i in range(2,N+1):
    for j in range(1,i+1):
        if i - j**2 > 0:
            dp[i] = min(dp[j**2] + dp[i-j**2], dp[i])
        elif i - j**2 == 0:
            dp[i] = 1
        
print(dp[N])


# 1 -> 1                1
# 2 -> 1^2 + 1^2        2
# 3 -> dp[2] + dp[1]    3
# 4 -> 2^2              1

# 5 -> 2^2 + 1          2
# 6 -> dp[5] + dp[1]    3
# 7 -> 
# 8
# 9 


# 25 
# 29 25 + 4