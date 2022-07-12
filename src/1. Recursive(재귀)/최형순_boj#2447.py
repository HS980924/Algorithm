'''
def draw_star(N:int):
    if(N == 3):
        for i in range(3):
            for j in range(3):
                if(i == 1 and j == 1):
                    continue
                else:
                    Map[i][j] = '*'
        return

    a = N//3
    draw_star(a)
    for i in range(3):
        for j in range(3):
            if (i == 1 and j == 1):
                continue
            else:
                for k in range(a) :
                    Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

def Print_Star(N:int):
    
    for i in range(N):
        for j in range(N):
            print(Map[i][j], end = '')
        print()

    return 

if __name__ == "__main__":
    N = int(input())
    Map = [[' ' for i in range(N)] for j in range(N)]
    draw_star(N)
    Print_Star(N)
'''
def draw_star(N:int, x:int, y:int):
    if(N == 3):
        for i in range(x,x+3):
            for j in range(y,y+3):
                if(i % 3 == 1 and j % 3 == 1):
                    continue
                else:
                    Map[i][j] = '*'
        return

    a = N//3
    for i in range(3):
        for j in range(3):
            if (i == 1 and j == 1):
                continue
            else:
                draw_star(a,x+i*a,y+j*a)

def Print_Star(N:int):
    
    for i in range(N):
        for j in range(N):
            print(Map[i][j], end = '')
        print()

    return 

if __name__ == "__main__":
    N = int(input())
    Map = [[' ' for i in range(N)] for j in range(N)]
    draw_star(N,0,0)
    Print_Star(N)
