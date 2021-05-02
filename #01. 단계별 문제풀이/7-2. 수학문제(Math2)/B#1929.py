'''
import math
M, N = map(int,input().split())
# M <= x <= N

for i in range (M,N+1):
    for j in range ()
'''
import math

def isPrime(N:int):
    if N == 1:
        return False
    for j in range(2,int(math.sqrt(N))+1):
        if(N % j == 0):
            return False
    return True

if __name__ == "__main__":
    M, N = map(int,input().split())

    for i in range(M,N+1):
        if(isPrime(i)):
            print(i)

'''
def prime_sieve(M, N):
    isPrime = [True] * (N + 1)
    isPrime[0], isPrime[1] = False, False

    for base in range(2, int(N ** (1 / 2)) + 1, 1):
        if isPrime[base]:
            isPrime[base * base::base] = [False] * ((N // base) - base + 1)

    for i in range(M, N + 1):
        if isPrime[i]:
            print(i)

m, n = map(int, input().split())
prime_sieve(m, n)
'''

