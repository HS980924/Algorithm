# 1 <= num <= 1,000
def fun(num):
    count = 0
    arr = []
    if(num >= 100):
        count = 99
        for i in range (100,num+1):
            arr.append(i)
            arr = list(str(i))
            arr = list(map(int,arr))
            d = arr[1] - arr[0]
            for i in range (len(arr)-1):
                if(arr[i+1] == arr[i] + d):
                    fact = True
                    continue
                else:
                    fact = False
                    break
            if (fact == True):
                count += 1
    else:
        count = num

    return count


if __name__ == "__main__":
    num = int(input())
    N = fun(num)
    print(N)

#승현이 코드
'''
def func(a:int):
    
    if a>=100:
        count = 0
        arr = list(str(a))
        if (int(arr[0])-int(arr[1]))==(int(arr[1])-int(arr[2])):
            return 1
        else:
            return 0
    elif a==1000:
        return 0
    else:
        return 1

if __name__=="__main__":
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        ans+=func(i)
    print(ans)
'''

# 한수 구하기
'''
N = int(input(""))
hansu = 0
for i in range(1,N+1):
    if i <= 99:
        hansu += 1
    else :
        num = list(str(i))
        if(int(num[0]) - int(num[1]) == int(num[1]) - int(num[2])):
            hansu += 1
print(hansu)
'''