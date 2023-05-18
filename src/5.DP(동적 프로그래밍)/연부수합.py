def solution(elements):
    answer = 0
    sum_list = {}
    maxLength = len(elements)
    dp = [0 for _ in range(maxLength)]
    
    for length in range(1,maxLength):
        for i in range(maxLength):
            idx = (i+length-1)%maxLength
            dp[i] += elements[idx]
            sum_list[dp[i]] = dp[i]
    maxValue = dp[0] + elements[-1]
    sum_list[maxValue] = maxValue 
    answer = len(sum_list)
    
    
    return answer


elements = [7,9,1,1,4]
print(solution(elements))


# MAXSUM = sum(elements)
# sum_list[MAXSUM] = MAXSUM