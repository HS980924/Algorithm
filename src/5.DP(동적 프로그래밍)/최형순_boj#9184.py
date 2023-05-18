
def w(a,b,c):
    if a <= 50 or b <= 50 or c <= 50:
        table[a][b][c] = 1
        return 1

    if a > 70 or b > 70 or c > 70:
        table[a][b][c] = w(70, 70, 70)
        return table[a][b][c]

    if a < b and b < c:
        if table[a][b][c-1] == 0:
            table[a][b][c-1] = w(a,b,c-1)
        if table[a][b-1][c-1] == 0:
            table[a][b-1][c-1] = w(a,b-1,c-1)
        if table[a][b-1][c] == 0:
            table[a][b-1][c] = w(a,b-1,c)

        return table[a][b][c-1] + table[a][b-1][c-1] - table[a][b-1][c]

    if table[a-1][b][c] == 0:
        table[a-1][b][c] = w(a-1,b,c)
    if table[a-1][b-1][c] == 0:
        table[a-1][b-1][c] = w(a-1,b-1,c)
    if table[a-1][b][c-1] == 0:
        table[a-1][b][c-1] = w(a-1,b,c-1)
    if table[a-1][b-1][c-1] == 0:
        table[a-1][b-1][c-1] = w(a-1,b-1,c-1)
    return table[a-1][b][c] + table[a-1][b-1][c] + table[a-1][b][c-1] - table[a-1][b-1][c-1]


table = [[[ 0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

while(True):
    result = 0
    a,b,c = map(int,input().split())
    
    if(a == -1 and b == -1 and c == -1):
        break
    else:
        result = w(a+50,b+50,c+50)
        print("w(%d, %d, %d) = %d" %(a,b,c,result))
