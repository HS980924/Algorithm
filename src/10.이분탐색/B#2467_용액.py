# Upload BOJ Gold-5 TwoPointer & BinarySearch 용액
N = int(input())
lst = list(map(int,input().split()))
lst.sort()
answer = []
sumMax = 1000000000*2

left = 0
right = N-1

while left < right:
    curSum = lst[left] + lst[right]
    
    if abs(curSum) <= abs(sumMax):
        answer = [lst[left], lst[right]]
        sumMax = curSum
    
    if curSum < 0:
        left += 1
    elif curSum > 0:
        right -= 1
    else:
        break

print(*answer)
        



