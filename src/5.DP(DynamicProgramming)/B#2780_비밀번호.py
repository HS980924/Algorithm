# Upload BOJ Silver-1 DP 2780번 비밀번호
import sys
input = sys.stdin.readline

testCase = int(input())
password = [[1,2,3],[4,5,6],[7,8,9]]
ways = [[-1,0],[0,1],[1,0],[0,-1]]
neighborNums = [[] for _ in range(10)]

neighborNums[0].append(7)
neighborNums[7].append(0)

for i in range(1,10):
    x = (i-1)//3 
    y = (i-1)%3
    for way in ways:
        nx = x + way[0]
        ny = y + way[1]
        if 0 <= nx < 3 and 0 <= ny < 3:
            neighborNums[i].append(password[nx][ny])

for _ in range(testCase):
    N = int(input())
    dp = [[0 for _ in range(N+1)] for _ in range(10)]
    for i in range(10):
        dp[i][1] = 1
    
    for i in range(2,N+1):
        for j in range(10):
            for num in neighborNums[j]:
                dp[j][i] += dp[num][i-1]
            dp[j][i] %= 1234567
            
    sum = 0
    for i in range(10):
        sum += dp[i][N]
    print(sum % 1234567)