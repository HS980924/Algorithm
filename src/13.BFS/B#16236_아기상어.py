from collections import deque

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
answer = 0

def bfs(x,y):
    sharkSize = 2
    result = 0
    eatCnt = 0
    fishEat = []
    ways = [[-1,0],[0,-1],[1,0],[0,1]]
    cntMaps = [[0]*N for _ in range(N)]

    while True:
        queue = deque()
        queue.append([x,y])
        
        while queue:
            row, col = queue.popleft()

            if maps[row][col] < sharkSize and 0 < maps[row][col] < 9:
                fishEat.append([cntMaps[row][col],row,col])

            for i in range(4):
                nx, ny = row + ways[i][0], col + ways[i][1]
                if 0 <= nx < N and 0 <= ny < N:
                    if maps[nx][ny] <= sharkSize and not cntMaps[nx][ny]:
                        cntMaps[nx][ny] = cntMaps[row][col] + 1
                        queue.append([nx,ny])

        if len(fishEat) > 0:
            fishEat.sort()
            maps[x][y] = 0
            x, y = fishEat[0][1], fishEat[0][2]
            maps[x][y] = 9
            result += fishEat[0][0]
            eatCnt += 1
            cntMaps = [[0]*N for _ in range(N)]
            if eatCnt == sharkSize:
                sharkSize += 1
                eatCnt = 0           
            fishEat = []
        else:
            break
    return result

def solution(N):
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 9:
                answer = bfs(i,j)
                return answer

print(solution(N))