# Upload BOJ Silver-5 BinarySearch 10815번 숫자카드
N = int(input())
cards1 = list(map(int,input().split()))

M = int(input())
cards2 = list(map(int,input().split()))
cards1.sort()
answer = []

def binarySearch(num):
    start = 0
    end = N-1
    
    while start <= end:
        mid = (start+end)//2
        
        if cards1[mid] < num:
            start = mid + 1
        elif cards1[mid] > num:
            end = mid - 1
        else:
            return 1
        
    return 0

for value in cards2:
    answer.append(binarySearch(value))

print(*answer)

