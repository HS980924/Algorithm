# Upload BOJ Silver-3 BinarySearch 7795번 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

T = int(input())

def BS(value:int, M:int):
    left = 0
    right = M-1
    
    while left <= right:
        mid = (left+right) // 2
        
        if B[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

for _ in range(T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    result = 0
    A.sort()
    B.sort()
    
    for value in A:
        idx = BS(value,M)
        result += (idx+1)
    print(result)
    

