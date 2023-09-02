# Upload BOJ Silver-4 Greedy & Sort ATM
N = int(input())
times = list(map(int,input().split()))

times.sort()

answer = 0
before = 0

for x in times:
    answer += x + before
    before += x

print(answer)

