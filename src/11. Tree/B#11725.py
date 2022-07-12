def dfs(visited, tree, start):
    visited[1] = False
    result = [0]*(N+1)
    queue = []
    
    for x in tree[start]:
        result[x] = start
        queue.append(x)

    while queue:
        v = queue.pop(0)
        if visited[v]:
            visited[v] = False
            for i in tree[v]:
                if visited[i]:
                    result[i] = v
                    visited[i] = False
                    for s in tree[i]:
                        queue.append(s)
    
    return result

N = int(input())
visited = [True]*(N+1)
tree = [[] for i in range(N+1)]

for i in range(N-1):
    v1, v2 = map(int,input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

print(tree)
result = dfs(visited,tree,1)
print(result)
