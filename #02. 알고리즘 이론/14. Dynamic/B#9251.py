input1 = list(input())
input2 = list(input())

dp = [[0 for _ in range(len(input1)+1)] for _ in range(len(input2)+1)]
for i in range(1,len(input2)+1):
    for j in range(1,len(input1)+1):
        if (input1[j-1] == input2[i-1]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp)
print(max(max(dp)))




