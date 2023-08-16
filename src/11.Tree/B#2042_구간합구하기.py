# Upload BOJ Gold-1 Segment Tree 2042번 구간 합 구하기
import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
arr = []
tree = [0]*(N*4)

def init(start, end, idx):
    
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1,end,idx*2+1)
    return tree[idx]

def interval_sum(start, end, idx, left, right):
    
    if left > end or right < start:
        return 0
    
    if start >= left and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2
    
    return interval_sum(start,mid,idx*2,left, right) + interval_sum(mid+1,end,idx*2+1,left,right)

def update(start, end, idx, what, value):
    
    if what < start or what > end:
        return
    tree[idx] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx*2, what, value)
    update(mid+1, end, idx*2+1, what, value)


for i in range(N):
    arr.append(int(input()))
    
init(0,len(arr)-1,1)

for i in range(M+K):
    a, b, c = map(int,input().split())
    
    if a == 1:
        value = c- arr[b-1]
        arr[b-1] = c
        update(0,len(arr)-1,1,b-1,value)
    else:
        print(interval_sum(0,len(arr)-1,1,b-1,c-1))
