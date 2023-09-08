# def solution(arrayA, arrayB):
#     answer = 0
#     answer_a = 0
#     answer_b = 0
    
#     arrayA.sort()
#     arrayB.sort()
    
#     a_divisorList = getDivisor(arrayA[0])
#     b_divisorList = getDivisor(arrayB[0])
    
#     for a_value in a_divisorList:
#         check_a = True
#         check_b = True
#         for x in arrayA:
#             if x % a_value != 0:
#                 check_a = False
#                 break
#         for y in arrayB:
#             if y % a_value == 0:
#                 check_b = False
#                 break
#         if check_a and check_b:
#             answer_a = max(a_value,answer_a)
            
#     for b_value in b_divisorList:
#         check_a = True
#         check_b = True
#         for x in arrayB:
#             if x % b_value != 0:
#                 check_a = False
#                 break
#         for y in arrayA:
#             if y % b_value == 0:
#                 check_b = False
#                 break
#         if check_a and check_b:
#             answer_b = max(b_value,answer_b)

#     answer = max(answer_a,answer_b)
#     if answer == 1:
#         answer = 0
#     return answer

# def result(arr,arrayA,arrayB):
#     answer = 0
#     for a_value in arr:
#         check_a = True
#         check_b = True
#         for x in arrayA:
#             if x % a_value != 0:
#                 check_a = False
#                 break
#         for y in arrayB:
#             if y % a_value == 0:
#                 check_b = False
#                 break
#         if check_a and check_b:
#             answer = max(a_value,answer)
            
#     return answer

# def getDivisor(num):
#     arr = []
#     result = []
#     for i in range(1,int(num**0.5)+1):
#         if num % i == 0:
#             arr.append(i)
    
#     for x in arr:
#         result.append(x)
#         result.append(num//x)
#     return result

from math import gcd

def get_gcd(arr):
    g = arr[0]
    for i in range(len(arr)):
        g = gcd(g,arr[i])
    
    return g

def solution(arrayA,arrayB):
    answer = 0
    gcd_a, gcd_b = get_gcd(arrayA), get_gcd(arrayB)
    
    print(gcd_a,gcd_b)
    
    for b in arrayB:
        if not b % gcd_a:
            break
    else:
        answer = max(answer,gcd_a)
    
    for a in arrayA:
        if not a % gcd_b:
            break
    else:
        answer = max(answer,gcd_b)
    
    return answer



array_A = [10, 20]
array_B = [5, 20]

print(solution(array_A,array_B))