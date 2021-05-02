#골든바흐의 추측(B#9020)
import math 

if __name__ == "__main__":
    T = int(input())
    tmp = 10000
    pri = []
    prime=[False,False]+[True]*(tmp-1)
    for i in range(2,int(tmp**0.5)+1):
        if prime[i]:
            for j in range(2*i,tmp+1,i):
                prime[j]=False
    for i in range(len(prime)):
        if(prime[i]):
            pri.append(i)

    for i in range (T):
        N = int(input())
        for i in range(len(pri)):
            if(pri[i] > N/2):
                ind = i-1
                break
        i = ind
        j = ind
        while(True):
            if(pri[i] + pri[j] > N):
                i -= 1
                j = i
            elif(pri[i] + pri[j] == N):
                print(pri[i],end = ' ')
                print(pri[j])
                break
            else:
                j += 1

'''
import sys
input = sys.stdin.readline

max_number= 10000
prime=[False,False,]+[True]*(max_number - 1)
for i in range(2,int(max_number**0.5)+1):
    if prime:
        for j in range(2*i,max_number+1,i):
            prime[j] = False

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    for i in range(n//2,1,-1):
        if prime[i] and prime[n-i]:
            print(i, n-i)
            break
'''
'''
import sys

MAX_N = 10000

eratos = [True] * (MAX_N+1)
eratos[0], eratos[1] = False, False
for i in range(2, MAX_N+1):
    if eratos[i]:
        for j in range(2*i, MAX_N+1, i):
            eratos[j] = False
    
for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    for a in range(n//2, 0, -1):
        b = n-a
        if eratos[a] and eratos[b]:
            print(a, b)
            break
'''