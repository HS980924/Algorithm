import math 
T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    X_s= abs(x1 - x2)
    Y_s= abs(y1 - y2)
    P_s = math.sqrt((X_s*X_s) + (Y_s*Y_s))

    if(P_s == 0):
        if(r1 != r2):
            print(0)
        else:
            print(-1)
    else:
        if(P_s > r1+r2):
            print(0)
        elif(P_s == r1 + r2):
            print(1)
        else:
            if(P_s == abs(r1-r2)):
                print(1)
            elif(P_s < abs(r1-r2)):
                print(0)
            else:
                print(2)
