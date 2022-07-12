
'''
def Quick_Sort(left:int, right:int):
    pl = left
    pr = right
    pivot = int((pl+pr)/2)
    mid = Num[pivot]

    while(pl <= pr):
        while(Num[pl] < mid):
            pl += 1
        while(Num[pr] > mid):
            pr -= 1
        if(pl <= pr):
            tmp = Num[pl]
            Num[pl] = Num[pr]
            Num[pr] = tmp
            pl += 1
            pr -= 1

    if(left < pr):
        Quick_Sort(left,pr)
    if(pl < right):
        Quick_Sort(pl,right)
    
    return 
'''  
if __name__ == "__main__":
    N = int(input())
    Num = []

    for i in range(N):
        Num.append(int(input()))

    Num.sort()  
    for i in sorted(Num):
        print(i)
