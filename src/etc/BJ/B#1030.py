import sys
s,N,K,r1,r2,c1,c2 = map(int,input().split())
print(s,N,K,r1,r2,c1,c2)
board = [[1 for i in range(N**s)] for _ in range(N**s)]

print(board)


def solution(n,k,s,x,y):
    if s == 1:
        for i in range(x,x+n):
            for j in range(y,y+n):
                if (i % k >= n-k-1 and j % k >= n-k-1) and (i % k <= k and j % k <= k) :
                    continue
                else:
                    board[i][j] = 0
    else:
        print("ASDASd")
        for i in range(n):
            for j in range(n):
                if ( i <= k or i >= n-k-1) and (j <= k or j >= n-k-1):
                    continue
                else:
                    solution(n,k,s-1,x+n*i,x+n*j)

def PRINT(r1,r2,c1,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            print(board[i][j],end='')
        print()

solution(N,K,s,0,0)
PRINT(r1,r2,c1,c2)