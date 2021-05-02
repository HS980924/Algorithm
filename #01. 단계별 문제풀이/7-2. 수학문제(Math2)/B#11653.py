'''
import math

N = int(input())
pri = []

for i in range (2,N+1):
    status = 0
    if(i == 1):
        continue
    for j in range (2, int(math.sqrt(i)) + 1):
        if(i % j == 0):
            status = 1
            break
    if(status == 0):
        if(N % i == 0):
            pri.append(i)

i = 0
while(N > 1):
    if(N % pri[i] == 0):
        print(pri[i])
        N = N / pri[i]
    else:
        i += 1
'''
'''
N = int(input())
i = 2
while(N > 1):
        if(N % i == 0):
            print(i)
            N = N / i
        else:
            i += 1
'''
n = int(input())
i = 2
while (n >= i*i):
    if n % i == 0:
        n //= i
        print(i)
    else:
        i += 1
if n != 1:
    print(int(n)) 

'''
import math

n=int(input())
for i in range(2,int(math.sqrt(n))+1):
    while n%i==0:
        print(i)
        n//=i
if n>1:
    print(n)
'''