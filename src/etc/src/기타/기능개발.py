def solution(progresses, speeds):
    answer = []
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        cnt = 0
        while progresses != [] and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:                
            answer.append(cnt)
        
    return answer

# def solution(progresses, speeds):
#     answer = []
#     index = 0
    
#     while index < len(progresses):
#         for i in range(len(progresses)):
#             progresses[i] += speeds[i]
        
#         cnt = 0
#         while index < len(progresses) and progresses[index] >= 100:
#             index += 1
#             cnt += 1
            
#         if cnt != 0:  
#             answer.append(cnt)
        
#     return answer
pro = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]	
print(solution(pro,s))