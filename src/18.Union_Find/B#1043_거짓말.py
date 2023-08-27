# Upload BOJ Gold-4 Union-Find 1043번 거짓말
# 참고 블로그 : https://my-coding-notes.tistory.com/471
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
info = list(map(int,input().split()))
tree = [x for x in range(N+1)]
parties  = []

def Find(value):
    if value == tree[value]:
        return tree[value]
    tree[value] = Find(tree[value])
    return tree[value]

def Union(x,y):
    x = Find(x)
    y = Find(y)
    
    if x < y:
        tree[y] = x
    else:
        tree[x] = y

# 진실을 아는 사람들의 부모 노드를 0으로 설정
for value in info[1:]:
    tree[value] = 0
    
for _ in range(M):
    party = list(map(int,input().split()))
    parties.append(party[1:])
    
    if party[0] != 1:
        for i in range(1,party[0]):
            Union(party[i],party[i+1])

answer = 0
for party in parties:
    check = True
    for value in party:
        if Find(value) == 0:
            check = False
    if check:
        answer += 1
print(answer)

