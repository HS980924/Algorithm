def solution(n):
    answer = 0
    fibo = [0]*(n+1)
    fibo[0] = 1
    fibo[1] = 1

    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    return fibo[n] % 1000000007
n = 4
print(solution(n))