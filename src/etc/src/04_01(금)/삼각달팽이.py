def solution(n):
    answer = []
    arr = [[0 for x in range(y)] for y in range(1,n+1)]
    num = 1
    x = -1
    y = 0
    
    for i in range(n):
        for j in range(n-i):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            arr[x][y] = num
            num += 1
    
    for ele in arr:
        answer += ele
    
    return answer

# def solution(n):
#     answer = []
#     tmp = [[0 for x in range(n)] for y in range(n)]
    
#     cnt = n
#     sum = 1
#     x, y = -1, 0
#     while cnt != 0:
#         for k in range(cnt):
#             x += 1
#             tmp[x][y] = sum
#             sum += 1
#         cnt -= 1
#         if cnt == 0:
#             break
#         for k in range(cnt):
#             y += 1
#             tmp[x][y] = sum
#             sum += 1
#         cnt -= 1
#         if cnt == 0:
#             break
#         for k in range(cnt):            
#             x -= 1
#             y -= 1
#             tmp[x][y] = sum
#             sum += 1
#         cnt -=1
        
        
#     for x in tmp:
#         for y in x:
#             if y != 0:
#                 answer.append(y)
#     return answer


print(solution(4))