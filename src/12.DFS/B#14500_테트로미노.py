# Uplaod BOJ Gold-4 DFS 14500번 테트로미노
# 참고 블로그 : https://cijbest.tistory.com/87
# 내 풀이 -> 모든 모양을 리스트에 담아서 for문으로 순차적으로 모양을 탐색 -> 초기 설정 값 귀찮음
R, C = map(int,input().split())
boards = [list(map(int,input().split())) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
moves = [[0,1],[0,-1],[1,0],[-1,0]]

answer = 0

def tetromino(x,y,totalSum, cnt):
    global answer
    
    if cnt == 4:
        answer = max(answer, totalSum)
        return
    
    for move in moves:
        nx = x+move[0]
        ny = y+move[1]
        
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            visited[nx][ny] = 1
            tetromino(nx,ny,totalSum+boards[nx][ny], cnt+1)
            visited[nx][ny] = 0

def exception(x,y):
    global answer
    for n in range(4):
        tmp = boards[x][y]
        for k in range(3):
            t = (n+k)%4
            nx = x+moves[t][0]
            ny = y+moves[t][1]
            
            if not (0 <= nx < R and 0 <= ny < C):
                tmp = 0
                break
            tmp += boards[nx][ny]
        answer = max(answer, tmp)

for i in range(R):
    for j in range(C):
        visited[i][j] = 1
        tetromino(i,j,boards[i][j],1)
        visited[i][j] = 0
        exception(i,j)
        
print(answer)

# L 모양 회전
# [0,0], [1,0], [2,0], [2,1],
# [0,0], [1,0], [0,1], [2,0],
# [0,0], [0,1], [1,1], [2,1],
# [0,0], [1,0], [1,-1], [1,-2]
# L 모양 대칭
# [0,0], [1,0], [2,0], [2,-1]
# [0,0], [0,1], [1,0], [2,0]

# ㅡ 모양
# [0,0],[0,1],[0,2],[0,3]
# [0,0],[1,0],[2,0],[3,0]

# ㅁ 모양
# [0,0],[0,1],[1,0],[1,1]

# ㄴㄱ 모양
# [0,0], [1,0], [1,1], [2,1]
# [0,0], [0,1], [-1,1], [-1,2]
# [0,0], [1,0], [1,-1],[2,-1]
# [0,0], [0,1], [1,1], [1,2]

# ㅗ 모양
# [0,0], [0,1], [1,1] ,[0,2]
# [0,0], [1,0], [1,-1], [2,0]
# [0,0], [0,1], [-1,1], [0,2]
# [0,0], [1,0], [1,1], [2,0]
