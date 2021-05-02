while(True):
    x = list(map(int,input().split()))

    x1 = max(x)
    x2 = min(x)
    x3 = sum(x)-(x1+x2)
    if(x3 == 0 and x2 == 0 and x1 == 0):
        break
    elif(x1*x1 == x2*x2 + x3*x3):
        print('right')
    else:
        print('wrong')