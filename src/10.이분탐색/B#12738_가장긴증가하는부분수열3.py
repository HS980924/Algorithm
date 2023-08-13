# Upload BOJ Gold-2 BinarySearch 12738번 가장긴증가하는부분수열3
N = int(input())
suyeul = list(map(int,input().split()))
lis = [suyeul[0]]

for value in suyeul[1:]:
    if lis[-1] < value:
        lis.append(value)
    else:
        start = 0
        end = len(lis) - 1
        
        while start < end:
            mid = (start+end) // 2
            
            if lis[mid] < value:
                start = mid + 1
            else:
                end = mid
                
        lis[end] = value

print(len(lis))