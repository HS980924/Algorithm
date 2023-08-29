# Upload BOJ Gold-4 Union-Find 1976번 여행 가자
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

tree = [x for x in range(N+1)]

def Find(idx):
    if idx == tree[idx]:
        return tree[idx]
    tree[idx] = Find(tree[idx])
    return tree[idx]

def Union(x, y):
    x = Find(x)
    y = Find(y)
    
    if x == y:
        return
    elif x < y:
        tree[y] = x
    else:
        tree[x] = y
    

for i in range(N):
    city_info = list(map(int,input().split()))
    for j in range(len(city_info)):
        if city_info[j]:
            Union(i+1,j+1)
            
path = list(map(int,input().split()))

possible = True
check = tree[path[0]]

for value in path:
    if check != tree[value]:
        possible = False
        break
    
if possible:
    print("YES")
else:
    print('NO')
