import sys

N = int(input())
linkArr = [0]*(N+1)
edges = []
D_cnt = 0
G_cnt = 0

for i in range(N-1):
    v1, v2 = map(int,sys.stdin.readline().split())
    linkArr[v1] += 1
    linkArr[v2] += 1
    edges.append([v1,v2])

for i in range(1,N+1):
    G_cnt += linkArr[i] * (linkArr[i] - 1) * (linkArr[i] - 2) / 6 if linkArr[i] >= 3 else 0
# 두 노드의 link 수를 이용하여 ㄷ트리를 구한다.
for a, b in edges:
    D_cnt += (linkArr[a] - 1) * (linkArr[b] - 1)

if  G_cnt*3 < D_cnt:
    print("D")
elif G_cnt*3 > D_cnt:
    print("G")
elif G_cnt*3 == D_cnt:
    print("DUDUDUNGA")