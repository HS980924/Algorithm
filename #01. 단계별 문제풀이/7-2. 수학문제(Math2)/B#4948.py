import math
def isPrime(N:int):
    n=2*N
    a = [False,False] + [True]*(n-1)
    primes=[]
    count = 0
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    for i in range(len(primes)):
        if (primes[i] > N and primes[i] <= 2*N):
            count += 1
    return count 

while(True):
    N = int(input())
    if(N == 0):
        break
    else:
      print(isPrime(N))
'''
def inspection(a):
    if a == 1:
        return 0
    else :
        for i in range(2,int((a**0.5)+1)):
            if a%i==0:
                return 0
        return 1

if __name__=="__main__":
    arr=[]
    for i in range(1,123456*2):
        if inspection(i)==1:
            arr.append(i)
    while True:
        N = int(input())
        if N == 0:
            break
        count = 0
        for j in range(len(arr)):
            if arr[j] > N and arr[j] <= 2*N:
                count+=1
        print(count)
'''

'''
sieve = [1 for i in range(123456*2 + 1)]
for i in range(2, 123457):
    if sieve[i] == 0:
        continue
    for j in range(2 * i, 123456 * 2 + 1, i):
        sieve[j] = 0
        
n = int(input())
while n != 0:

    print(sum(sieve[n +1 : 2*n + 1]))
    n = int(input())

'''

'''
tmp = 123456*2
prime=[False,False]+[True]*(tmp)
for i in range(2,int(tmp**0.5)+1):
    if prime[i]:
        for j in range(2*i,tmp+1,i):
            prime[j]=False

while True:
    n = int(input())
    if n == 0:
        break
    print(prime[n+1:2*n+1].count(True))
'''