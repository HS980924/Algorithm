# 2022.05.26(목)
# 뱀 - Queue 문제
# 문제 링크 : https://www.acmicpc.net/problem/3190

N = int(input())
loc_cnt = int(input())
board = []
for i in range(N+2):
    tmp = []
    for j in range(N+2):
        if j == 0 or j == N+1 or i == 0 or i == N+1:
            tmp.append(3)
        else:
            tmp.append(0)
    board.append(tmp)
board[1][1] = 2

for i in range(loc_cnt):
    x, y = map(int, input().split())
    board[x][y] = 1
    
change_dir = {}
direc_cnt = int(input())
for i in range(direc_cnt):
    x, y = map(str,input().split())
    change_dir[int(x)] = y

time = 0
dir = [[0,1],[1,0],[0,-1],[-1,0]]
dir_index = 0
snake = []
snake.append([1,1])

def is_over():
    global dir_index
    result = False
    checkLoc_x = snake[-1][0] + dir[dir_index][0]
    checkLoc_y = snake[-1][1] + dir[dir_index][1]
    if board[checkLoc_x][checkLoc_y] >= 2:
        result = True
    return result

def change_direct():
    global dir_index
    x = dir[dir_index][0]
    y = dir[dir_index][1]
    if dir_index % 2 == 0:
        if change_dir[time] == "D":
            dir_index = dir.index([y,x])
        else:
            dir_index = dir.index([-y,x])
    else:
        if change_dir[time] == "D":
            dir_index = dir.index([y,-x])
        else:
            dir_index = dir.index([y,x])

while True:
    time += 1
    if is_over():
        break
    else:
        head_loc = [x+y for x,y in zip(dir[dir_index],snake[-1])]
        snake.append(head_loc)
        if board[head_loc[0]][head_loc[1]] != 1:
            tail_loc = snake.pop(0)
            board[tail_loc[0]][tail_loc[1]] = 0
        board[head_loc[0]][head_loc[1]] = 2
        if time in change_dir:
            change_direct()

print(time)        