# Upload BOJ Gold-5 Greedy 1092번 배
import sys

input = sys.stdin.readline

N = int(input())
cranes = list(map(int,input().split()))
M = int(input())
containers = list(map(int,input().split()))

cranes.sort(reverse=True)
containers.sort(reverse=True)
time = 0

if cranes[0] < containers[0]:
    print(-1)
else:
    while containers:
        for crane in cranes:
            for container in containers:
                if crane >= container:
                    containers.remove(container)
                    break
        time += 1
    print(time)