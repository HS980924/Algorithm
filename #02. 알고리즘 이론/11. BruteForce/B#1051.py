N, M = map(int,input().split())

tri = []
for i in range(N):
    s = list(map(int,input()))
    tri.append(s)

area = [1]
for i in range(N):
    for k in range(M):
        x = tri[i][k]
        pos1 = k
        Length = 0
        for j in range(k,M):
            if tri[i][j] == x and j != pos1:
                pos2 = j
                Length = pos2 - pos1
                if i + Length < N:
                    if tri[i+Length][pos1] == x and tri[i+Length][pos2] == x:
                        ss = (Length+1)*(Length+1)
                        area.append(ss)
                else:
                    break

print(max(area))