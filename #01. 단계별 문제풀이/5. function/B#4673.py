def d(n):
    NumSum = 0
    arr = list(str(n))
    arr = list(map(int,arr))
    NumSum = sum(arr) + n
    return NumSum

if __name__ == "__main__":
    SelfNum = []
    None_SelfNum = []
    for i in range (10001):
        SelfNum.append(i)
        None_SelfNum.append(d(i))

    None_SelfNum.sort()
    None_SelfNum = set(None_SelfNum)
    SelfNum = set(SelfNum)
    SelfNum = (SelfNum-None_SelfNum)
    SelfNum = list(map(int,SelfNum))
    SelfNum.sort()
    for i in range (len(SelfNum)):
        print(SelfNum[i])

'''
def d(n):
    NumSum = 0
    arr = list(str(n))
    arr = list(map(int,arr))
    NumSum = sum(arr) + n
    return NumSum

if __name__ == "__main__":
    SelfNum = []
    for i in range (10001):
        SelfNum.append(d(i))
    
    SelfNum.sort()

    for i in range(1,10000):
        if i in SelfNum:
            continue
        else:
            print(i)
'''