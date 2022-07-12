# 시간 초과 답안
# -----------------------------------------------------------------------------------------
# from itertools import combinations

# def solution(clothes):
#     answer = 0
#     hash = {}
    
#     for x in clothes:
#         if hash.get(x[1]):
#             hash[x[1]] += 1
#         else:
#             hash[x[1]] = 1
    
#     for i in range(1,len(hash)+1):
#         tmp = list(combinations(list(hash.values()),i))
#         for x in tmp:
#             sum = 1
#             for i in range(len(x)):
#                 sum *= x[i]
#             answer += sum
#     return answer

# -----------------------------------------------------------------------------------------

# 참고 링크 : https://coding-grandpa.tistory.com/88

def solution(clothes):
    answer = 1
    hash = {}
    
    for value, key in clothes:
        hash[key] = hash.get(key,0) + 1
        
    for key in hash:
        answer *= (hash[key]+1)
    
    answer -= 1
    
    return answer

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))