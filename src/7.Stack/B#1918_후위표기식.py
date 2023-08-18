# Upload BOJ Gold-2 Stack 1918번 후위표기식
# exp = input()
# op = {
#     "+":1,
#     "-":1,
#     "*":2,
#     "/":2,
#     "(":3,
#     ")":3,
# }
# operator = []
# operand = []
# answer = ""


# for value in exp:
#     print("oprand:", operand)
#     print("oprator:", operator)
#     print("-------------------")
#     if value in op:
#         if not operator:
#             operator.append(value)
#         else:
#             if value == ")":
#                 while operator[-1] != "(":
#                     num1 = operand.pop() 
#                     num2 = operand.pop() 
#                     result = num2 + num1 + operator.pop()
#                     operand.append(result)
#                 operator.pop()
#             else:
#                 while operator and op[operator[-1]] >= op[value] and operator[-1] != '(':
#                     num1 = operand.pop() 
#                     num2 = operand.pop() 
#                     result = num2 + num1 + operator.pop()
#                     operand.append(result)
#                 operator.append(value)
#     else:
#         operand.append(value)

# while operator:
#     num1 = operand.pop()
#     num2 = operand.pop()
#     result = num2 + num1 + operator.pop()
#     operand.append(result)

# print(operand.pop())



exp = input()
op = {
    "+":1,
    "-":1,
    "*":2,
    "/":2,
    "(":3,
    ")":3,
}
stack = []
result = ""

for value in exp:
    if value in op:
        if value == "(":
            stack.append(value)
        else:
            if value == ")":
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
            else:
                while stack and op[stack[-1]] >= op[value] and stack[-1] != "(":
                    result += stack.pop()
                stack.append(value)
    else:
        result += value

while stack:
    result += stack.pop()
print(result)
