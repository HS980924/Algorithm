'''
# 8 <= N,M <= 50
# 8*8 크기
def Check_Board(n,m):
    cnt1 = 0
    cnt2 = 0
    for i in range(n,n+8):
        for j in range(m,m+8):
            if(j + i) % 2 == 0:
                if Ches[i][j] != 'W':
                    cnt1 += 1
                if Ches[i][j] != 'B':
                    cnt2 += 1
            else:
                if Ches[i][j] != 'B':
                    cnt1 += 1
                if Ches[i][j] != 'W':
                    cnt2 += 1
    
    return cnt1 if(cnt1 <= cnt2) else cnt2

if __name__ == "__main__":
    N, M = map(int,input().split())
    Ches = [ list(input()) for _ in range(N)]
    Num = []
    
    for i in range(N-7):
        for j in range(M-7):
            count = Check_Board(i,j)
            Num.append(count)

    print(min(Num))
'''
'''
def Check_Board(x:int, y:int):
    cnt_B = 0
    cnt_W = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if(i % 2 == 0):
                if(j % 2 == 0):
                    if(Board[i][j] != 'W'):         # WB
                        cnt_W += 1
                    if(Board[i][j] != 'B'):         # BW
                        cnt_B += 1
                else:
                    if(Board[i][j] != 'B'):         # WB
                        cnt_W += 1
                    if(Board[i][j] != 'W'):         # BW
                        cnt_B += 1
            else:
                if(j % 2 == 0):
                    if(Board[i][j] != 'W'):         # BW
                        cnt_B += 1
                    if(Board[i][j] != 'B'):         # WB
                        cnt_W += 1
                else:
                    if(Board[i][j] != 'B'):         # BW
                        cnt_B += 1
                    if(Board[i][j] != 'W'):         # WB
                        cnt_W += 1
    return cnt_B if(cnt_B <= cnt_W) else cnt_W


if __name__ == "__main__":
    N, M = map(int,input().split())

    Board = [list(input()) for _ in range (N)]
    Board_Cnt = []

    for i in range (N-7):
        for j in range(M-7):
            count = Check_Board(i,j)
            Board_Cnt.append(count)

    print(min(Board_Cnt))
'''
def Check_Board(x,y):
    cnt1 = 0
    cnt2 = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if(j + i) % 2 == 0:
                if Board[i][j] != 'W':
                    cnt1 += 1
                if Board[i][j] != 'B':
                    cnt2 += 1
            else:
                if Board[i][j] != 'B':
                    cnt1 += 1
                if Board[i][j] != 'W':
                    cnt2 += 1
    
    return cnt1 if(cnt1 <= cnt2) else cnt2

if __name__ == "__main__":
    N, M = map(int,input().split())
    Board = [ list(input()) for _ in range(N)]
    Board_Cnt = []
    
    for i in range(N-7):
        for j in range(M-7):
            count = Check_Board(i,j)
            Board_Cnt.append(count)

    print(min(Board_Cnt))


