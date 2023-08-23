# Upload BOJ Gold-5 Union-Find 1717번 집합의 표현
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
tree = [ x for x in range(N+1)]

def Find(idx):
    if idx == tree[idx]:
        return tree[idx]
    
    tree[idx] = Find(tree[idx])
    return tree[idx]
    
def Union(x,y):
    x = Find(x)
    y = Find(y)
    
    if x < y:
        tree[x] = y
    elif x > y:
        tree[y] = x
    else:
        return

def isUnion(x,y):
    x = Find(x)
    y = Find(y)
    
    return x == y

for _ in range(M):
    exp, a, b = map(int,input().split())
    
    if exp:
        # 포함 여부 확인
        if isUnion(a,b):
            print('YES')
        else:
            print('NO')
    else:
        # 합집합 연산
        Union(a,b)