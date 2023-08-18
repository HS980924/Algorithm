# Upload BOJ Gold-5 Stack 2504번 괄호의 값 
# exp = input()
# result = ""
# stack = []
# operator = []
# beforeValue = ""
# op = {
#     ")":"(",
#     "]":"[",
#     "(": 2,
#     "[": 3, 
# }


# for value in exp:
#     if value in ["(","["]:
#         stack.append(value)
#         if beforeValue:    
#             if beforeValue in ["(", "["]:
#                 operator.append("*")
#             else:
#                 operator.append("+")
#         operator.append("(")
#         result += str(op[value])
#     else:
#         if stack[-1] == op[value]:
#             stack.pop()
#             while operator[-1] != "(":
#                 result += operator.pop()
#             operator.pop()
#         else:
#             break
#     beforeValue = value

# if stack:
#     print(0)
# else: 
#     num_stack = []
#     for value in result:
#         if value == '*':
#             num1 = num_stack.pop()
#             num2 = num_stack.pop()
#             num_stack.append(num1 * num2)
#         elif value == '+':
#             num1 = num_stack.pop()
#             num2 = num_stack.pop()
#             num_stack.append(num1 + num2)
#         else:
#             num_stack.append(int(value))
#     print(num_stack[0])

#

bracket = input()
stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):
    
    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)