def dfs(numbers, target, result):
    cnt = 0
    if numbers == []:
        if result == target:
            return 1
        else:
            return 0
    else:
        cnt += dfs(numbers[1:],target,result+numbers[0])
        cnt += dfs(numbers[1:],target,result-numbers[0])
        return cnt

def solution(numbers, target):
    answer = dfs(numbers,target,0)
    return answer 

# def solution(numbers, target):
#     answer = DFS(numbers, target, 0)
#     return answer

# def DFS(numbers, target, depth):
#     answer = 0
#     if depth == len(numbers):
#         print(numbers)
#         if sum(numbers) == target:
#             return 1
#         else: return 0
#     else:
#         answer += DFS(numbers, target, depth+1)
#         numbers[depth] *= -1
#         answer += DFS(numbers, target, depth+1)
#         return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers,target))
