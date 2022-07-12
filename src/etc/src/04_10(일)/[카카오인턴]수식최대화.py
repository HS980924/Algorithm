from itertools import permutations

def operate(num1, num2, oper):
    if oper == '*':
        return num1 * num2
    elif oper == '+':
        return num1 + num2
    else:
        return num1 - num2

def filter(exp):
    arr = []
    tmp = ''
    for x in exp:
        if str(x).isdigit():
            tmp += x
        else:
            arr.append(tmp)
            arr.append(x)
            tmp = ''
    if tmp:
        arr.append(tmp)
    
    return arr

def calculator(exp,op):
    arr = exp[:]
    for oper in op:
        stack = []
        while len(arr) != 0:
            tmp = arr.pop(0)
            if tmp == oper:
                result = operate(int(stack.pop()), int(arr.pop(0)),oper)
                stack.append(result)
            else:
                stack.append(tmp)
        arr = stack
    
    return abs(int(arr[0]))
    

def solution(expression):
    op = ["*","-","+"]
    op = list(permutations(op,3))
    answer = []
    exp = filter(expression)
    for x in op:
        res = calculator(exp,x)
        answer.append(res)
    
    return max(answer)

expression = "100-200*300-500+20"
print(solution(expression))