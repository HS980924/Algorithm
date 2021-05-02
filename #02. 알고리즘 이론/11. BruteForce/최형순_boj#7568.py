N = int(input())
x = []
y = []

for i in range(N):
    Weight, Height = list(map(int,input().split()))
    x.append(Weight)
    y.append(Height)

for i in range(N):
    rank = 1
    for j in range(N):
        if(i == j):
            continue
        if(x[i] < x[j] and y[i] < y[j]):
            rank += 1
    print(rank, end = ' ')


'''
# group = [ list(map(int,input().split())) for _ in range(N)]

group = []
for i in range(N):
    x,y = map(int,input().split())
    group.append([x,y])

'''