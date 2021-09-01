N = int(input())

linkarr = [0]
result = [0]*(N+1)
trust = [True]*(N+1)
queue = []

for i in range(N):
    linkarr.append(list(map(int,input().split())))

upo = int(input())
start = list(map(int,input().split()))

for i in range(len(start)):
    queue.append(start[i])
    trust[start[i]] = False

while queue != []:
    pass