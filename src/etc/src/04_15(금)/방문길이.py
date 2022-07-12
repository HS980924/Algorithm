def solution(dirs):
    answer = 0
    check = []
    x,y = 0,0 
    
    
    for dir in dirs:
        tmp_x, tmp_y = x, y
        if dir == "U":
            tmp_y += 1
        elif dir == "L":
            tmp_x -= 1
        elif dir == "R":
            tmp_x += 1
        else:
            tmp_y -= 1
        
        if abs(tmp_x) <= 5 and abs(tmp_y) <= 5:
            if (x,y,tmp_x,tmp_y) not in check:
                answer += 1
                check.append((x,y,tmp_x,tmp_y))
                check.append((tmp_x,tmp_y,x,y))
            x, y = tmp_x, tmp_y
            
    return answer


dirs = "ULURRDLLU"
print(solution(dirs))