# Upload BOJ Gold-4 Union-Find 20040번 사이클 게임
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
tree = [x for x in range(N)]
answer = 1000001

def find(idx):
    if idx == tree[idx]:
        return idx
    tree[idx] = find(tree[idx])
    return tree[idx]

def Union(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    if x < y:
        tree[x] = y
    else:
        tree[y] = x

def isUnion(x,y):
    x = find(x)
    y = find(y)
    
    return x == y

for i in range(1,M+1):
    x, y = map(int,input().split())
    if isUnion(x,y):
        answer = min(answer,i)
    Union(x,y)

print(answer % 1000001)