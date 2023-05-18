N = int(input())

for i in range(N):
    VPSList = []
    VPS = input()
    
    for x in VPS:
        if x == '(':
            VPSList.append(x)
        else:
            if VPSList and VPSList[-1] == '(':
                VPSList.pop()
            else:
                VPSList.append(x)
                break

    if VPSList:
        print("NO")
    else:
        print("YES")