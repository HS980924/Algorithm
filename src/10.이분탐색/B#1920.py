import sys

N = int(input())
ip = list(map(int,sys.stdin.readline().split()))

M = int(input())
op = list(map(int,sys.stdin.readline().split()))

ip.sort()

for x in op:
    left = 0
    right = len(ip) - 1
    result = 0

    while(left <= right):
        mid = (left + right) // 2
        if(ip[mid] < x):
            left = mid + 1
        elif(ip[mid] > x):
            right = mid - 1
        elif(ip[mid] == x):
            result = 1
            break

    print(result)