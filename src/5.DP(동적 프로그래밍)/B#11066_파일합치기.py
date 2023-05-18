T = int(input())

for case in range(T):
    N = int(input())
    files = [0] + list(map(int,input().split()))
    
    DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
    S = [0 for _ in range(N+1)]
    
    for i in range(1,N+1):
        S[i] = S[i-1] + files[i]
    
    for i in range(2,N+1): # 부분 길이 (2 ~ N)
        for j in range(1,N+2-i): # 시작 지점
            tmp = []
            for k in range(i-1):
                tmp.append(DP[j][j+k] + DP[j+k+1][j+i-1])
            DP[j][j+i-1] = min(tmp) + (S[j+i-1] - S[j-1])
    
    print(DP[1][N])
