# Upload BOJ Gold-4 BFS&DFS 알파벳
# import sys

# input = sys.stdin.readline
# R, C = map(int, input().split())
# board = [list(input().strip()) for _ in range(R)]
# ways = [[0,1],[1,0],[-1,0],[0,-1]]
# maxCnt = 0
# visited = dict()
# for i in range(26):
#     visited[chr(65+i)] = 0

# def dfs(x, y, cnt):
#     global maxCnt
#     maxCnt = max(maxCnt, cnt)
    
#     for i in range(4):
#         nx, ny = x+ways[i][0], y+ways[i][1]
        
#         if 0 <= nx < R and 0 <= ny < C and not visited[board[nx][ny]]:
#             visited[board[nx][ny]] = 1
#             dfs(nx,ny,cnt+1)
#             visited[board[nx][ny]] = 0

# visited[board[0][0]] = 1
# dfs(0,0,1)

# print(maxCnt)
######################################

import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
ways = [[0,1],[1,0],[-1,0],[0,-1]]

def bfs(x, y, cnt):
    queue = set([(x,y,board[x][y])])
    
    while queue:
        x, y, path = queue.pop()
        for i in range(4):
            nx, ny = x+ways[i][0], y+ways[i][1]
            
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in path:
                queue.add((nx,ny,path+board[nx][ny]))
                cnt = max(cnt, len(path)+1)
    return cnt
            

print(bfs(0,0,1))