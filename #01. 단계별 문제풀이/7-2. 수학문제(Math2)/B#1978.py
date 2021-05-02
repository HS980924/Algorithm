N = int(input())

p = list(map(int,input().split()))

count = 0
for i in range (len(p)):
    if(p[i] == 1):
        count += 1
    else:
        for j in range (2,p[i]):
            if(p[i] % j == 0):
                count += 1
                break
            
print(N-count)

'''
N = int(input())
x = list(map(int, input().split()))

sum = len(x)
for i in x:
    if i == 1:
        sum -= 1
        continue
    for j in range(2, i):
        if i % j == 0:
            sum -= 1
            break
print(sum)
'''