def solution(prices):
    answer = [0]*len(prices)
    stack_idx = []
    
    for i in range(len(prices)):
        for x in stack_idx:
            answer[x] += 1
            
        while stack_idx and prices[stack_idx[-1]] > prices[i]:
            stack_idx.pop()
        
        stack_idx.append(i)
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))