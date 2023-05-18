def Fun(res, M, N):
    global result
    op = 0
    if(M == N):
        result.append(res)
        return
    else:
        for i in range(4):
            if Oper[i]:
                op = res
                if(i == 0):
                    res = res + A[M]
                elif(i == 1):
                    res = res - A[M]
                elif(i == 2):
                    res = res * A[M]
                else:
                    if(res < 0):
                        res = -res
                        res = res // A[M]
                        res = -res
                    else:    
                        res = res // A[M]
                Oper[i] -= 1     
                Fun(res,M+1,N)
                Oper[i] += 1
                res = op

if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split()))
    Oper = list(map(int,input().split()))
    result = []

    Fun(A[0],1,N)

    print(max(result))
    print(min(result))