import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Tree = [[] for _ in range(N+1)]

for i in range(N):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1, 2):
        Tree[temp[0]].append((temp[i], temp[i+1]))


def bfs(index):
    visit = [-1] * (N+1)
    q = deque([index])
    visit[index] = 0
    Max = [0, 0]

    while q:
        old = q.popleft()
        for i in Tree[old]:
            if visit[i[0]] == -1:
                visit[i[0]] = visit[old] + i[1]
                q.append(i[0])
                if Max[0] < visit[i[0]]:
                    Max[0] = visit[i[0]]
                    Max[1] = i[0]
    return Max

value, f_node = bfs(1)
answer, e_node2 = bfs(f_node)
print(answer)