from collections import deque
import sys
input = sys.stdin.readline
queue = []
direc = [[0,0,1],[0,1,0],[0,0,-1],[0,-1,0],[1,0,0],[-1,0,0]]

def check(next_loc, building, L, R, C):
    if next_loc[0] < 0 or next_loc[0] >= L:
        return False
    if next_loc[1] < 0 or next_loc[1] >= R:
        return False
    if next_loc[2] < 0 or next_loc[2] >= C:
        return False
    if building[next_loc[0]][next_loc[1]][next_loc[2]] == '#':
        return False
    return True

def BFS(building, L, R, C):
    global q
    tmp_queue = []
    time = 0
    result = False
    while q:
        loc = q.popleft()
        if building[loc[0]][loc[1]][loc[2]] == "E":
            result = True
            break
        else:
            building[loc[0]][loc[1]][loc[2]] = '#'
            for i in range(6):
                next_loc = [x+y for x,y in zip(direc[i],loc)]
                if check(next_loc, building, L, R, C):
                    tmp_queue.append(next_loc)
            if queue == []:
                time += 1
                queue = tmp_queue.copy()
                tmp_queue = []
    
    return [time, result]

while True:
    time = 0
    L, R, C = map(int, input().split())
    if L + R + C == 0:
        break
    else:
        building = []
        q = deque
        for i in range(L):
            tmp1 = []
            for j in range(R):    
                tmp2 = list(input().strip())
                if "S" in tmp2:
                    q.append([i,j,tmp2.index('S')])
                tmp1.append(tmp2)
            input()
            building.append(tmp1)
        
        result = BFS(building, L, R, C)
        if result[1]:
            print("Escaped in" +  str(result[0]) + "minute(s)")
        else:
            print("Trapped!")
        
        
        
    
