# Upload BOJ Gold-5 math 14891번 톱니바퀴
gears = [[]]

for _ in range(4):
    gears.append(list(map(int,input())))
    
K = int(input())

def moveGear(ways):
    for num, move in ways:
        if move == 1:
            tmp = gears[num][7]
            for i in range(7):
                gears[num][7-i]= gears[num][7-(i+1)]
            gears[num][0] = tmp
        else:
            tmp = gears[num][0]
            for i in range(7):
                gears[num][i]= gears[num][i+1]
            gears[num][7] = tmp
            
for _ in range(K):
    num, move = map(int,input().split())

    move_gears = []
    move_gears.append([num,move])
    
    left_num = num - 1
    right_num = num + 1
    currentLeftMove = move
    currentRightMove = move
    
    while left_num >= 1:
        if gears[left_num+1][6] != gears[left_num][2]:
            move_gears.append([left_num,-currentLeftMove])
            left_num -= 1
            currentLeftMove *= -1
        else:
            break
        pass
    while right_num <= 4:
        if gears[right_num-1][2] != gears[right_num][6]:
            move_gears.append([right_num,-currentRightMove])
            right_num += 1
            currentRightMove *= -1
        else:
            break
    moveGear(move_gears)

answer = 0
for i in range(1,5):
    if gears[i][0] == 1:
        answer += 2**(i-1)
print(answer)
    