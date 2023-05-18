def solution(order):
    answer = 0
    box_order = [0]*len(order)
    stack = []
    
    for i in range(len(order)):
        box_order[order[i]-1] = i+1
    
    for x in box_order:
        if x == answer+1:
            answer += 1
            while stack and stack[-1] == answer+1:
                stack.pop(-1)
                answer += 1
        else:
            stack.append(x)

    return answer


order =[4, 3, 1, 2, 5]
print(solution(order))