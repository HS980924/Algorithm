def solution(number, k):
    answer = ''
    number = list(number)
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    answer = "".join(stack[:len(stack)-k])        
    return answer

# def solution(number, k):
#     answer = ''
#     length = len(number) - k
#     number = list(number)
    
#     while length > 0:
#         tmp = number[:]
#         print(tmp)
#         while True:
#             value = max(tmp)
#             print(value)
#             ind = number.index(value)
#             if len(number)-ind >= length:
#                 answer += value
#                 number.remove(value)
#                 break
#             else:
#                 tmp.remove(value)
#         length -= 1
    
#     return answer

n = "4177252841"
k = 4
print(solution(n,k))