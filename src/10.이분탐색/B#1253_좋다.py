# Upload BOJ Gold-4 BinarySearch 좋다
N = int(input())
numbers = list(map(int,input().split()))
answer = 0
numbers.sort()

for i in range(N):
    tmp = numbers[:i] + numbers[i+1:] 
    left = 0
    right = N-2
    while left < right:
        numSum = tmp[left] + tmp[right]
        if numSum == numbers[i]:
            answer += 1
            break
        elif numSum < numbers[i]:
            left += 1
        else:
            right -= 1
            
print(answer)