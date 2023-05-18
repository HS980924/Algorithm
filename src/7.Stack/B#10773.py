import sys

List = []

N = int(input())

for i in range(N):
    Money = int(sys.stdin.readline())

    if(Money == 0):
        List.pop()
    else:
        List.append(Money)

print(sum(List))


