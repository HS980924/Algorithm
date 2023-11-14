# Upload BOJ silver-1 implement 16926번 배열돌리기1
N, M, R = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(R):
    for j in range(min(N,M)//2):
        x, y = j, j
        pre = arr[x][y]
        
        for i in range(x+1, N-j):
            tmp = arr[i][j]
            arr[i][j] = pre
            pre = tmp
        
        for i in range(y+1,M-j):
            tmp = arr[N-1-j][i]
            arr[N-1-j][i] = pre
            pre = tmp
        
        for i in range(N-j-2,j-1,-1):
            tmp = arr[i][M-1-j]
            arr[i][M-1-j] = pre
            pre = tmp
        
        for i in range(M-2-j,j-1,-1):
            tmp = arr[j][i]
            arr[j][i] = pre
            pre = tmp
for i in range(N):
    print(*arr[i])