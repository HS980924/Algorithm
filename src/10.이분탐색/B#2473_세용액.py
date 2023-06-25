# Upload BOJ Gold-3 TwoPointer & BinarySearch 세용액
N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

def Solutions(liquids):
    answer = []
    sumMax = 4000000000
    
    for i in range(N-2):
        res = liquids[i]
        left = i+1
        right = N-1
        
        while left < right:
            curSum = res + liquids[left] + liquids[right]
            if abs(curSum) <= abs(sumMax):
                answer = [res, liquids[left], liquids[right]]
                sumMax = curSum
            if curSum < 0:
                left += 1
            elif curSum > 0:
                right -= 1
            else:
                return answer
    return answer

print(*Solutions(liquids))