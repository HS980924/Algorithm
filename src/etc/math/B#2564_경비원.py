# Upload BOJ Silver-1 implement 2564번 경비원
col, row = map(int,input().split())
location = []
SUM = 0
M = int(input())

for _ in range(M+1):
    x, y = map(int,input().split())
    if x == 1:
        location.append([1,y])
    elif x == 2:
        location.append([row+1,y])
    elif x == 3:
        location.append([y+1,0])
    else:
        location.append([y+1,col])
        
for i in range(M):
    nx, ny = location[i][0], location[i][1]
    x, y = location[-1][0], location[-1][1]
    
    if nx == x:
        if abs(ny-y) == col:
            SUM += 2*min(nx-1,row+1-nx)
        SUM += abs(ny-y)
    else:
        x_Length = abs(nx-x)
        y_Length = min(ny + y, (col-ny)+(col-y))
        SUM += x_Length + y_Length

print(SUM)