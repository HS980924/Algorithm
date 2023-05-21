# Upload BOJ GOld-4 DP 가장 긴 바이토닉 부분 수열

N = int(input())
suyul = list(map(int,input().split()))

dp_up = [ 1 for _ in range(N)]
dp_dw = [ 1 for _ in range(N)]
result = [ 0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if suyul[i] > suyul[j]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)
        if suyul[N-i-1] > suyul[N-j-1]:
            dp_dw[N-i-1] = max(dp_dw[N-i-1], dp_dw[N-j-1]+1)

for i in range(N):
    result[i] = dp_up[i] + dp_dw[i] - 1

print(max(result))
