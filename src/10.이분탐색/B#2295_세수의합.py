# Upload BOJ Gold-4 BinarySearch 2295번 세수의 합
# 참고 블로그 : https://konghana01.tistory.com/299

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
arrSum = []

for i in range(N):
    for j in range(i,N):
        arrSum.append(arr[i]+arr[j])
        
arrSum.sort()
answer = 0

for i in range(N):
    for j in range(i,N):
        res = arr[j] - arr[i]
        left = 0
        right = len(arrSum)-1
    
        while left <= right:
            mid = (left+right) // 2
            
            if res < arrSum[mid]:
                right = mid-1
            elif res > arrSum[mid]:
                left = mid+1
            else:
                answer = max(answer,arr[j])
                break
print(answer)







# 1 2 3 ...98 100 102
# 