'''
M = int(input())
N = int(input())
pri = []

for i in range (M,N+1):
    status = 0
    if(i == 1):
        continue
    else:
        for j in range (2,i):
            if(i % j == 0):
                status = 1
                break
        if(status == 0):
            pri.append(i)

if(len(pri) == 0):
    print(-1)
else:
    print(sum(pri))
    print(min(pri))
'''
import math
M = int(input())
N = int(input())
a = [2,3,5,7]
pri = []

for i in range (M,N+1):
    status = 0
    if(i == 1):
        continue
    for j in range (2, int(math.sqrt(i)) + 1):
        if(i % j == 0):
            status = 1
            break
    if(status == 0):
        pri.append(i)
if(len(pri) == 0):
    print(-1)
else:
    print(sum(pri))
    print(min(pri))

