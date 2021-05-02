# ====================================
#            DP Practice01
# ====================================
def bino(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return bino(n-1, k-1) + bino(n-1, k)

def fibo(N):
    table = [0]*(N+1)
    table[1] = 1
    table[2] = 1

    for i in range(3,N+1):
        table[i] = table[i-1] + table[i-2]
    
    return table[N]

def bino(n,k):

    cache = [[1]*(n+k) for _ in range(n+k)]
    
    for i in range(n+1):
        for k in range(i+1):
            if(i>= 1 or k >= 1):
                cache[i][k] = cache[i-1][k-1] + cache[i-1][k]
        
    
    return cache[n][k]



print(fibo(11))
print(bino(3,3))