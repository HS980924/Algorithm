def solution(board, moves):
    answer = 0
    space = [0]
    for index in moves:
        for i in range(len(board[index-1])):
            if board[i][index-1] != 0:
                space.append(board[i][index-1])
                board[i][index-1] = 0
                if space[-1] == space[-2]:
                    space.pop(-1)
                    space.pop(-1)
                    answer += 2
                break
    

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))


# 0 0 0 0 0   
# 0 0 1 0 3 
# 0 2 5 0 1
# 4 2 4 4 2
# 3 5 1 3 1






def solution(board, moves):
    box = []
    delete = 0
    for i in moves :
        for j in range(len(board[1])):
            if board[j][i-1] != 0 :
                box.append(board[j][i-1])
                board[j][i-1] = 0 
                break
        if len(box) >= 2 and box[-1] == box[-2]:
            box.pop()
            box.pop()
            delete += 2
    return delete



