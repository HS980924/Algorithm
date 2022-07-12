import heapq

def solution(scoville,K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        heapq.heappush(scoville,num1+num2*2)
        answer += 1
        
    return answer 
    
    

scoville = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(scoville,k))

# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while min(scoville) < K:
#         if len(scoville) <= 1:
#             return -1
#         num1 = scoville.pop(0)
#         num2 = scoville.pop(0)
#         newSco = num1 + (num2*2)
#         scoville.append(newSco)
#         index = len(scoville)-1
#         while True:
#             if scoville[index] < scoville[(index-1)//2]:
#                 tmp = scoville[index]
#                 scoville[index] = scoville[(index-1)//2]
#                 scoville[(index-1)//2] = tmp
#                 index = (index-1)//2
#             else:
#                 break
#         if scoville[index] < scoville[index+1]:
#             tmp = scoville[index]
#             scoville[index] = scoville[index+1]
#             scoville[index+1] = tmp
#         answer += 1
#     return answer