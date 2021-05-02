N = int(input())
Fibo = [0,1]

for i in range(2,N+1):
    Fibo.append(Fibo[i-1] + Fibo[i-2])

print(Fibo[N])