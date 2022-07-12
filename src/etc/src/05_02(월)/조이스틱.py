def solution(name):
    answer = 0
    
    for x in name:
        loc = 0
        next_loc = ord(x)-65
        up_down = abs(next_loc-loc)
        left = next_loc + 1
        right = 25-next_loc + 1
        if up_down == 0:
            up_down = 1
        answer += min(up_down, left, right)
        print(min(up_down, left, right))
        
    return answer

name = "JEROEN"
print(solution(name))