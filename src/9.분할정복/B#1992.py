import sys
N = int(input())
Tree = []

for i in range(N):
    Tree.append(list(map(int,input())))

def QuadTree(x,y,size):
    if size == 1:
        if Tree[x][y] == 1:
            print("1",end='')
        else:
            print("0",end='')
        return

    else:
        for i in range(x,x+size):
            for j in range(y,y+size):
                if Tree[i][j] != Tree[x][y]:
                    size = size//2
                    print("(",end='')
                    QuadTree(x,y,size)
                    QuadTree(x,y+size,size)
                    QuadTree(x+size,y,size)
                    QuadTree(x+size,y+size,size)
                    print(")",end='')
                    return

        if Tree[x][y] == 1:
            print("1",end='')
        else:
            print("0",end='')
        return


QuadTree(0,0,N)
