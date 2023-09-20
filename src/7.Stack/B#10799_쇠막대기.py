# Upload BOJ Silver-2 Stack 10799번 쇠막대기

brackets = list(input())
stack = []
razer = 0
idx = 0
answer = 0

while idx < len(brackets)-1:
    if brackets[idx] == '(':
        if brackets[idx+1] == ')':
            razer += 1
            idx += 1
            answer += len(stack)
        else:
            stack.append(brackets[idx])
            answer += 1
    else:
        stack.pop()
    idx += 1
        
print(answer)
        
