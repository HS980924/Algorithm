def solution(s):
    answer = True
    stack = []

    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if stack != []:
                stack.pop()
            else:
                answer = False
                break       
    
    if stack != []:
        answer = False 
        
    return answer

s = "()()"
print(solution(s))