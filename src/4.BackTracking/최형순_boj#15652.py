def NM(N:int, M:int, cnt:int):
    if(cnt == M):
        print(' '.join(map(str,data)))
        return
    else:
        for i in range(N):
            if tmp[i]:
                continue
            else:
                for j in range(i):
                    tmp[j] = True
                data[cnt] = i+1
                NM(N,M,cnt+1)
                for j in range(N-1,i,-1):
                    tmp[j] = False
                


if __name__ == "__main__":
    N, M = map(int,input().split())
    tmp = [False]*N
    data = [0]*M
    NM(N,M,0)

'''
N, M = map(int, input().split())
candidate = [False]*N
out = []


def NM4(tmp, N, M):
    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i] > out[j]:
                return
    if tmp == M:
        print(" ".join(map(str, out)))
        return

    for i in range(len(candidate)):

        candidate[i] = True
        out.append(i + 1)
        NM4(tmp + 1, N, M)
        candidate[i] = False
        out.pop()


NM4(0, N, M)
'''