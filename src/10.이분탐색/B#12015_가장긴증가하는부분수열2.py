# Upload BOJ Gold-3 BinarySearch 12015번 가장긴증가하는부분수열2
N = int(input())
suyeul = list(map(int,input().split()))
lis = [0]

for value in suyeul:
    if lis[-1] < value:
        lis.append(value)
    else:
        start = 0
        end = len(lis) 
        
        while start < end:
            mid = (start + end) // 2
        
            if lis[mid] <= value:
                start = mid + 1
            else:
                end = mid
        lis[end] = value

print(len(lis)-1)