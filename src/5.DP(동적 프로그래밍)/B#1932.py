N = int(input())

Num = [[]for _ in range(N)]
Num_copy = [[]for _ in range(N)]
for i in range(N):
    Num[i] = list(map(int,input().split()))
    Num_copy[i] = Num[i].copy()

for i in range(N-1):
    for j in range(len(Num[i])):
        left = Num[i][j] + Num_copy[i+1][j]
        right = Num[i][j] + Num_copy[i+1][j+1]
        if(Num[i+1][j] < left):
            Num[i+1][j] = left
        if(Num[i+1][j+1] < right):
            Num[i+1][j+1] = right

result = max(Num[N-1])
print(result)