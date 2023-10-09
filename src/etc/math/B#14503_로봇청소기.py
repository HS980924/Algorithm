# Upload BOJ Gold-5 Implement 14503번 로봇 청소기

N, M = map(int,input().split())
r, c, d = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
ways = [[-1,0],[0,1],[1,0],[0,-1]]
visited[r][c] = 1
cnt = 1

while True:
    exit = True
    
    for i in range(4):
        nd = (d+3)%4
        nr = r + ways[nd][0]
        nc = c + ways[nd][1]
        d = nd
        
        if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 0:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                cnt += 1
                r, c = nr, nc
                exit = False
                break
    
    if exit:
        if maps[r-ways[d][0]][c-ways[d][1]] == 1:
            print(cnt)
            break
        else:
            r = r-ways[d][0]
            c = c-ways[d][1]