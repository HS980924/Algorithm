# Upload BOJ Gold-4 DP 팰린드롬

import sys
input = sys.stdin.readline

N = int(input())
numList=list(map(int,input().split()))
M = int(input())

dp=[[0 for _ in range(N)] for _ in range(N)]
answer = 0

for length in range(N):
    for start in range(N-length):
        end = start + length
        if start == end:
            dp[start][end] = 1
        elif numList[start] == numList[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1]:
                dp[start][end] = 1

for _ in range(M):
    start, end = map(int,input().split())
    print(dp[start-1][end-1])