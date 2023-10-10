# Upload BOJ Gold-5 Heap 18405번 경쟁적전염
import heapq

N, K = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
S, X, Y = map(int,input().split())

ways = [[-1,0],[1,0],[0,-1],[0,1]]
heap = []

for i in range(N):
    for j in range(N):
        if maps[i][j]:
            time = 0
            birus = maps[i][j]
            visited[i][j] = maps[i][j]
            heapq.heappush(heap,[time, birus, i, j])

while heap:
    time, birus, x, y = heapq.heappop(heap)

    for way in ways:
        nx, ny = x+way[0], y+way[1]
        
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if time+1 <= S:
                visited[nx][ny] = birus    
                heapq.heappush(heap,[time+1,birus,nx,ny])

print(visited[X-1][Y-1])




# 1000*200*200
# 400,000,000

