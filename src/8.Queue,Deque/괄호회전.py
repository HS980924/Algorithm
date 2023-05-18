from collections import deque

def solution(s):
    answer = 0
    dq = deque(s)
    
    for i in range(len(s)):
        if checking(dq):
            answer += 1
        dq.append(dq.popleft())
    
    return answer

def checking(s):
    stack = []
    dic = {
        '[':']',
        '(':')',
        '{':'}',
    }

    for x in s:
        if x == "[" or x == "(" or x == "{":
            stack.append(x)
        else:
            if stack and dic[stack[-1]] == x:
                stack.pop(-1)
            else:
                return False
    
    if stack:
        return False
    else:
        return True

s ="}}}"

print(solution(s))