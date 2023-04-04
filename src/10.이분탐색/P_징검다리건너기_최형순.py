# def solution(stones, k):
#     answer = max(stones)
    
#     for i in range(len(stones)-k):
#         kMaxValue = max(stones[i:i+k])
#         if answer > kMaxValue:
#             answer = kMaxValue
    
#     return answer

# right를 200,000,000 으로 초기화 할 때 효율성 통과
# right를 max(stones)를 하면 케이스 하나 효율성 통과 x

def solution(stones, k):
    left = 1
    right = 200000000
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                cnt += 1    
            else:
                cnt = 0
                
            if cnt >= k:
                break
                
        if cnt < k:
            left = mid + 1
        else:
            right = mid - 1
        
    return left
