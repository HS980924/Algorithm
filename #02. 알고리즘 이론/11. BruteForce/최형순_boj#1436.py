#   666  1666  2666  3666  4666  5666  6660 6661 ~ 6669 7666 8666 9666
# 10666 11666 12666 13666 14666 15666 1666x~           17666
Num = int(input())
cnt = 0
data = 666
while True:
    if '666' in str(data):
        cnt += 1
    if(cnt == Num):
        break
    data += 1
    
print(data)


'''
def six_check(x):
    while True :
        if x%10==6:
            return True
            break
        x=x//10
        if x==0:
            break
    return False 

def triple6(x):
    i=10
    result=0
    i_return=0
    while True:
        x=x//10
        if x<100:
            break
        if x%1000 == 666:
            result=x*i
            i_return=i
        i*=10
    arr=[result,i_return]
    return arr

n=int(input())

default = 666
count=0
plus=0
while count!=n:
    result=default+plus*1000
    if six_check(plus)==True:
        arr=triple6(result)
        if arr[0]!=0:
            for i in range(arr[1]):
                i=i+arr[0]
                count+=1
                if count==n:
                    result=i
                    break
            if count==n:
                break
            plus+=1
            result=default+plus*1000
    plus+=1
    count+=1
print(result)
'''


'''
N = int(input())

L = [666]

for k in range(1,5):
    for n in range(k):
        for i in range(10**(k-n)):
            for j in range(10**n):
                L.append(i*10**(3+n) + 666*10**n + j)

L = sorted(list(set(L)))
print(sorted(L)[N-1])
'''