size, num = map(int,input().split())
seq = list(map(int,input().split()))

for i in range(size):
    if seq[i] < num:
        print(seq[i], end = ' ')

