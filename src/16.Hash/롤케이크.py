# def solution(topping):
#     answer = 0
#     right = []
#     hash = {}
    
#     for key in topping:
#         if not key in hash:
#             hash[key] = 0
#         hash[key] += 1

    
#     while(len(right) <= len(hash)):
#         value = topping.pop(-1)
#         hash[value] -= 1
#         if not value in right:
#             right.append(value)
#         if not hash[value]:
#             del hash[value]
#         if len(right) == len(hash):
#             answer += 1
    
#     return answer

def solution(topping):
    answer = 0
    set_dic = set()
    hash = {}
    
    for key in topping:
        if not key in hash:
            hash[key] = 0
        hash[key] += 1
    
    while(len(set_dic) <= len(hash)):
        value = topping.pop(-1)
        hash[value] -= 1
        set_dic.add(value)
        if not hash[value]:
            del hash[value]
        if len(set_dic) == len(hash):
            answer += 1
    
    return answer



# topping = [1, 2, 3, 1, 4]
# print(solution(topping))