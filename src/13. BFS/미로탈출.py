from collections import deque
def solution(maps):
    answer = 0
    global cntMaps
    cntMaps = [[100*100+1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == 'L':
                bfs(row,col,maps)
        
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == 'S':
                answer += cntMaps[row][col]
            if maps[row][col] == 'E':
                answer += cntMaps[row][col]
                
    if answer >= 100*100+1:
        answer = -1
        
    return answer

def bfs(x,y,maps):
    ways = [[0,1],[0,-1],[1,0],[-1,0]]
    queue = deque()
    cntMaps[x][y] = 0
    queue.append([x,y])
    
    while queue:
        row, col = queue.popleft()
        
        for way in ways:
            new_row = row + way[0]
            new_col = col + way[1]
            if 0 <= new_row and new_row < len(maps) and 0 <= new_col and new_col < len(maps[0]):
                if cntMaps[new_row][new_col] == 100*100+1 and maps[new_row][new_col] != 'X':
                    cntMaps[new_row][new_col] = cntMaps[row][col] + 1
                    queue.append([new_row,new_col])

maps = ["SOEOL","XXXXO","OOOOO","OXXXX","OOOOO"]
print(solution(maps))