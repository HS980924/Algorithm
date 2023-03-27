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