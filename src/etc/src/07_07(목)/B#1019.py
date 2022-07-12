# 시간 초과
N = int(input())
page = [0]*10

for i in range(1,N+1):
    tmp = i
    while tmp:
        res = tmp%10
        page[res] += 1
        tmp = tmp//10
        
print(*page)
    
    