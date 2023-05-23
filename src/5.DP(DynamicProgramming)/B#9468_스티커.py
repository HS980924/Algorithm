# Upload BOJ Silver-1 DP 스티커

T = int(input())
for _ in range(T):
    N = int(input())
    stickers = [ list(map(int,input().split())) for _ in range(2)]
    DP = [[0]*len(stickers[0]) for _ in range(2)]
    for j in range(N):
        for i in range(2):
            if j == 0:
                DP[i][0] = stickers[i][0]
            elif j == 1:
                DP[i][j] = stickers[i][j] + DP[(i+1)%2][j-1]
            else:
                DP[i][j] = stickers[i][j] + max(DP[(i+1)%2][j-1], DP[(i+1)%2][j-2])
                
    print(max(DP[0][-1], DP[1][-1]))
    
    