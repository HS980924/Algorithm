
def NM(N:int, M:int, cnt:int):
    if(cnt == M):
        print(' '.join(map(str, data)))
        return
    else:
        for i in range (N):
            if tmp[i]:
                continue
            else:
                for j in range (i+1):
                    tmp[j] = True
                data[cnt] = i+1
                NM(N,M,cnt+1)
                for j in range (N-1,i,-1):
                    tmp[j] = False

if __name__ == "__main__":
    N,M = map(int,input().split())
    tmp = [False]*N
    data = [0]*M
    NM(N,M,0)

