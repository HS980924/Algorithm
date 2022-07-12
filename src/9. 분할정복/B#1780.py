N = int(input())
paper = []
plus = 0
zero = 0
minus = 0

for i in range(N):
    paper.append(list(map(int,input().split())))

def QuadTree(x, y, size):
    global plus
    global zero
    global minus

    if size == 1:
        if paper[x][y] < 0:
            minus += 1
        elif paper[x][y] > 0:
            plus += 1
        else:
            zero += 1
        return
    else:
        for i in range(x,x+size):
            for j in range(y,y+size):
                if paper[x][y] != paper[i][j]:
                    for k in range(0,size,size//3):
                        for l in range(0,size,size//3):
                            QuadTree(x+k,y+l,size//3)
                    return
        
        if paper[x][y] < 0:
            minus += 1
        elif paper[x][y] > 0:
            plus += 1
        else:
            zero += 1
        return

QuadTree(0,0,N)

print(minus)
print(zero)
print(plus)
