T = int(input())

Pado = [1,1,1,2,2]

for i in range(T):
    N = int(input())
    for i in range(len(Pado),N+1):
        Pado.append(Pado[i-1] + Pado[i-5])
    print(Pado[N-1])
