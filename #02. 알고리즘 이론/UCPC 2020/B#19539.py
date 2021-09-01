N = int(input())
H = list(map(int,input().split()))
sum_x = 0
day = sum(H) // 3

if sum(H) % 3 == 0:
    for x in H:
        sum_x += x // 2  
    if day <= sum_x:
        print("YES")
    else:
        print("NO")
else:
    print("NO")