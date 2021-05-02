def fun(N):
    global cnt
    while(N > 1):
        if(N % 3 == 0):
            N = N/3
        elif(N % 6 != 0):
            N = N-1
        elif(N % 2 == 0):
            N = N/2
        cnt += 1


if __name__ == "__main__":
    N = int(input())
    cnt = 0
    fun(N)
    print(cnt)