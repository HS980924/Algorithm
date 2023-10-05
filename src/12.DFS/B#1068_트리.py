# Upload BOJ Gold-5 DFS 1068번 트리
# 나와 비슷한 코드 및 비슷한 에러.. 77%까지 성공...
# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1068%EB%B2%88-%ED%8A%B8%EB%A6%ACPython
N = int(input())
infos = list(map(int,input().split()))
remove_node = int(input())
tree = [[] for _ in range(N)]
root = 0
answer = 0

for i in range(N):
    if infos[i] == -1:
        root = i
    else:
        tree[infos[i]].append(i)

def leafNodeCnt(node):
    global answer
    
    if not tree[node]:
        answer += 1
        return
    
    for value in tree[node]:
        if value == remove_node:
            if len(tree[node]) == 1:
                answer += 1
            else:
                continue
        else:
            leafNodeCnt(value)
    return

if root == remove_node:
    print(0)
else:
    leafNodeCnt(root)
    print(answer)