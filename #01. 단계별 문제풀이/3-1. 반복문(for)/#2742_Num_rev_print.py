num = input()
num = int(num)
# num = int(input())

for i in range(0, num):  #for i in range(num)
    print(num-i)
    
# 조민준
'''
N = int(input())

for i in range(N, 0, -1):
    print(i)
'''
# 규호형
''' 
N = input()
N = int(N)
a = []

for i in range(1, N + 1):
    a.append(i)

a.reverse()
for i in range(N):
    print(a[i])
'''
# 최재훈
'''
N = int(input())
res = []
for i in range(1, N+1):
    res.append(i)

res.sort(reverse=True)
for j in range(N):
    print(res[j])
'''


