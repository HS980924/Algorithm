N = int(input())

ans = 0
for i in range(N):
    M = i
    m = str(M)
    m = list(map(int,m))

    if(N == M + sum(m)):
        ans = M
        break

print(ans)
 
# M  = N - sum(m)
# 3
# 9 10  




