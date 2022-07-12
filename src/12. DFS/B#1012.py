import sys
sys.setrecursionlimit(10**9)

def search(row,col):
    if ((0 <= row) and (row < N)) and ((0 <= col) and (col < M)):
        if(Baechu[row][col] == 1):
            Baechu[row][col] = -1
            search(row,col-1)   # 왼쪽
            search(row,col+1)   # 오른쪽
            search(row-1,col)   # 위
            search(row+1,col)   # 아래
 
if __name__ == "__main__":

    Test_case = int(input())

    for i in range(Test_case):
        M, N, K = map(int,input().split())
        Baechu = [[0]*M for _ in range(N)]
        Count = 0

        for j in range(K):
            x,y = map(int,input().split())
            Baechu[y][x] = 1
        
        for row in range(N):
            for col in range(M):
                if Baechu[row][col] > 0:
                    search(row,col)
                    Count += 1
        
        print(Count)


        