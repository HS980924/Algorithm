'''
def Queen(N:int,M:int): 
    global Ches
    global cnt

    if(M == N):
        cnt += 1
        return
    else:
        for i in range(N):
            if(Check(N,M,i)):
                Ches[M][i] = True
                Queen(N,M+1)
                Ches[M][i] = False   
        return             

def Check(N:int, M:int, i:int):
    global Ches
    
    for j in range(N):              # 가로 체크 (굳이 안해도 됨)
        if Ches[M][j]:             
            return  False
    
    for j in range(N):              # 세로 체크
        if Ches[j][i]:
            return False

    x = M
    y = i
    while(x >= 0 and y >=0 ):       # 왼쪽 위 대각선 \
        if Ches[x][y]:
            return False
        else:
            x -= 1
            y -= 1

    x = M
    y = i
    while(x < N and y < N):         # 오른쪽 아래 대각선 \
        if Ches[x][y]:
            return False
        else:
            x += 1
            y += 1

    x = M
    y = i    
    while(x >= 0 and y < N):        # 왼쪽 아래 대각선  /
        if Ches[x][y]:
            return False
        else:
            x -= 1
            y += 1

    x = M
    y = i          
    while(x < N and y >= 0):        # 오른쪽 위 대각선  /
        if Ches[x][y]:
            return False
        else:
            x += 1
            y -= 1

    return True

if __name__ == "__main__":
    N = int(input())
    Ches = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    Queen(N,0)
    print(cnt)
'''
'''
def Check(x):
    for i in range(x):
        if posQ[x] == posQ[i] or abs(posQ[x] - posQ[i]) == x-i:
            return False    
    return True

def nQueen(x):
    global cnt

    if(x == N):
        cnt += 1
        return
    else:
        for i in range(N):
            posQ[x] = i
            if Check(x):
                nQueen(x+1)
           

N = int(input())
posQ = [0]*N
cnt = 0
nQueen(0)
print(cnt)
'''
'''
global cnt
global posQ
def nQueen(posQ:list, y:int):
    posQ.append(y)
    if len(posQ) >= 2:
        for i in range(len(posQ)-1):
            if y == posQ[i]:
                return 0
            if abs(posQ[i] - y) == (len(posQ) -1 - i):
                return 0

    if len(posQ) == N:
        return 1    
    
    cnt = 0
    for k in range(N):
        cnt += nQueen(posQ, k)
        posQ.pop()

    return cnt

    
if __name__ == "__main__":
    global N
    cnt = 0
    N = int(input())
    posQ = []

    for i in range(N):
        cnt += nQueen(posQ, i)
        posQ.pop()
    print(cnt)
'''