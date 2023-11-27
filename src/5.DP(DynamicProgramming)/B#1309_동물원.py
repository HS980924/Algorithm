# Upload BOJ Silver-1 DP 1309번 동물원
# 참고 블로그 : https://my-coding-notes.tistory.com/264

N = int(input())
dp = [1,3] + [0]*(N-1)
for i in range(2,N+1):
    dp[i] = (dp[i-2] + dp[i-1]*2)%9901
print(dp[N])