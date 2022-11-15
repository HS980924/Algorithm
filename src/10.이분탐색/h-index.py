def solution(citations):
    answer = 0
    left = 0
    right = max(citations)
    
    while(left <= right):
        mid = (left + right) // 2
        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= mid:
                cnt += 1
        if cnt >= mid and len(citations) - cnt <= mid:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    
    return answer

citations = [4,4,4]
print(solution(citations))