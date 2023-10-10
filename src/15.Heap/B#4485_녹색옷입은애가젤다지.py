# Upload BOJ Gold-4 Heap & Dijkstra 4485번 녹색 옷 입은 애가 젤다지
import sys, heapq

cnt = 1
ways = [[0,1],[1,0],[0,-1],[-1,0]]
INF = sys.maxsize

while True:
    N = int(input())
    
    if not N:
        break
    
    answer = 0
    maps = [list(map(int,input().split())) for _ in range(N)]
    
    def dijkstra(N):
        visited = [[INF for _ in range(N)] for _ in range(N)]
        heap = []
        heapq.heappush(heap,[maps[0][0],0,0])
        visited[0][0] = maps[0][0]
        
        while heap:
            rupee, x, y = heapq.heappop(heap)
            
            for way in ways:
                nx, ny = x+way[0], y+way[1]
                if 0 <= nx < N and 0 <= ny < N:
                    total_rupee = maps[nx][ny] + rupee
                    if visited[nx][ny] > total_rupee:
                        visited[nx][ny] = total_rupee
                        heapq.heappush(heap,[total_rupee,nx,ny])
        return visited[N-1][N-1]
    answer = dijkstra(N)
    
    print('Problem',str(cnt)+":",answer)
    cnt += 1