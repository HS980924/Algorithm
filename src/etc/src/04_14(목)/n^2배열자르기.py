# def solution(n, left, right):
#     answer = []
#     arr = []
    
#     for i in range(n):
#         tmp = []
#         for j in range(i+1):
#             tmp.append(i+1)
#         for j in range(i+1,n):
#             tmp.append(tmp[j-1]+1)
#         arr.append(tmp)
            
#     answer = sum(arr,[])
    
#     return answer[left:right+1]

# def solution(n, left, right):
#     answer = []
#     for i in range(left,right+1):
#         answer.append(max(i//n,i%n)+1)
#     return answer

def solution(n, left, right):
    answer = []

    
    for i in range(left,right+1):
        res = i%n
        step = i//n
        if res <= step:
            answer.append(step+1)
        else:
            answer.append(res+1)
            
        
    return answer

n = 4
left = 7
right = 14
print(solution(n,left,right))