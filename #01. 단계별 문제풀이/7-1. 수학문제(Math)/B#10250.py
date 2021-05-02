N = int(input())

for i in range (N):
    H,W,N = map(int,input().split())
    if(N % H == 0):
        Ho = N//H
    else:
        Ho = (N // H) + 1 #호수 XX
    if(Ho < 10):
        Ho = '0'+ str(Ho)
    else:
        Ho = str(Ho)
    Ch = N % H 
    if(Ch == 0):
        Ch = H
    Ch = str(Ch)
    print(Ch+Ho)
# YXX 또는 YYXX =>(층수)(호수)

# 재훈이
'''
T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())
    room = n//h+1
    floor = n%h
    if floor==0:
        floor=h
        room-=1
    print(floor*100+room)
'''

# 민준이
'''
T = int(input())

for i in range(T):
    count = 0
    H, W, N = map(int, input().split())
    for j in range(1,W+1):
        for k in range(1,H+1):
            count += 1
            if j < 10:
                if count == N:
                    print(str(k)+'0'+str(j))
                    break
            else:
                if count == N: 
                    print(str(k)+str(j))
                    break
'''

# 승현이
'''
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    print(H, end="") if N%H==0 else print((N%H),end="")
    print('%02d'%(N//H)) if N%H==0 else print('%02d'%int((N//H)+1))
'''
