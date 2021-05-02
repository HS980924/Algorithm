import math

tmp = 1000000
pri = [False,False] + [True]*(tmp-1)
for i in range(2,int(math.sqrt(tmp))+1):
    if pri[i]:
        for j in range(2*i,tmp,i):
            pri[j] = False
while(True):
    N = int(input())

    if(N == 0):
        break
    else:
        for a in range(N-1, 0, -1):
            b = N-a
            if pri[a] and pri[b]:
                print(N,"=",b,"+",a)
                break
            elif(a == 1):
                print("Goldbach's conjecture is wrong.")
                break

'''
import sys
prime = [True]*(1000001)
for i in range(2,1000001):
    if(prime[i]==True):
        for j in range(i+i,1000001,i):
            prime[j] = False
while True:
    n = int(sys.stdin.readline())
    if(n==0):
        break
    find = 0
    for i in range(3,1+(n//2),2):
        if(prime[i]==True and prime[n-i]==True):
            print('{} = {} + {}'.format(n,i,n-i))
            find = 1
            break
    if(find==0):
        print("Goldbach's conjecture is wrong.")
'''