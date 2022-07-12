def solution(s):
    stack = []
    
    for x in s:
        stack.append(x)
        print('before', stack)
        if len(stack) >= 2:
            if stack[len(stack)-1] == stack[len(stack)-2]:
                stack.pop(len(stack)-1)
                stack.pop(len(stack)-1)
    if not stack:
        return 1
    else:
        return 0

s = 'baabaa'
print(solution(s))