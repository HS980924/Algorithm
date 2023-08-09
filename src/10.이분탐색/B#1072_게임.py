# Upload BOJ Silver-3 BinarySearch 1072번 게임
X, Y = map(int,input().split())

Z = (Y*100)//X

if Z >= 99:
    print('-1')
else:
    start = 1
    end = 1000000000
    answer = 0
        
    while start <= end:
        mid = (start+end) // 2
        
        new_z = (mid+Y)*100 // (mid+X)

        if new_z <= Z:
            start = mid+1
        else:
            answer = mid
            end = mid-1
            
    print(answer)
    
# int(Y/X)*100 -> 틀림
# 부동소수점 오차 때문..?