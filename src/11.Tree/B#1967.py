import sys
N = int(input())
Tree = [[] for _ in range(N+1)]

for i in range(N-1):
    node = list(map(int,sys.stdin.readline().split()))
    Tree[node[0]].append([node[1], node[2]])
    Tree[node[1]].append([node[0], node[2]])


def dfs(Tree,start):
    visited = [-1]*(N+1)
    queue = []
    queue.append(start)
    visited[start] = 0
    distance = [0,0]

    while queue:
        v = queue.pop(0)
        for i in Tree[v]:
            if visited[i[0]] == -1:
                visited[i[0]] = visited[v] + i[1]
                queue.append(i[0])
                if distance[0] < visited[i[0]]:
                    distance[0] = visited[i[0]]
                    distance[1] = i[0]

    return distance

Max_distance, vertex1 = dfs(Tree, 1)
Max_distance, vertex2 = dfs(Tree, vertex1)

print(Max_distance)
