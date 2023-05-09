import sys
input = sys.stdin.readline

N = int(input())
numbers = [ int(input()) for _ in range(N)]
numbers.sort()

SUM = [0]*(N+1)
SUM[1] = numbers[0]

for i in range(2,N+1):
    SUM[i] = max(SUM[i-1]+numbers[i-1], (SUM[i-2] + numbers[i-2]*numbers[i-1]))

print(SUM[N])


