import sys


def quadTree(x,y,size):
    global zero
    global one

    if size == 1:
        if square[x][y] == 1:
            one += 1
        if square[x][y] == 0:
            zero += 1
        return

    for i in range(x,x+size):
        for j in range(y,y+size):
            if square[i][j] != square[x][y]:
                quadTree(x,y,size//2)
                quadTree(x+size//2,y,size//2)
                quadTree(x,y+size//2,size//2)
                quadTree(x+size//2,y+size//2,size//2)
                return
    
    if square[x][y] == 1:
        one += 1
    else:
        zero += 1
    return

N = int(input())
zero = 0
one = 0
square = []
for i in range(N):
    square.append(list(map(int,sys.stdin.readline().split())))
quadTree(0,0,N)

print(zero)
print(one)

