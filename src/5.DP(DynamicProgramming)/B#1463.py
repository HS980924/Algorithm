'''
N = int(input())
Num_count = [0]*(N+1)

for i in range(2,N+1):
    Num_count[i] = Num_count[i-1] + 1
    if i % 3 == 0 and Num_count[i//3] + 1 < Num_count[i]:
        Num_count[i] = Num_count[i//3] + 1
    if i % 2 == 0 and Num_count[i//2] + 1 < Num_count[i]:
        Num_count[i] = Num_count[i//2] + 1

print(Num_count[N])
'''