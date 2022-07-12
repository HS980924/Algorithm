# def solution(skill, skill_trees):
#     answer = 0
#     dic = {skill[i] : i for i in range(len(skill))}
    
#     for sk in skill_trees:
#         tmp = ""
#         check = False        
#         for x in sk:
#             if x in skill:
#                 tmp += x
#         if tmp == "":
#             check = True
#         else:
#             order = 0
#             for value in tmp:
#                 if dic[value] < order:
#                     check = True
#                 elif dic[value] == order:
#                     order += 1
#                     check = True
#                 else:
#                     check = False
#                     break
            
#         if check:
#             answer += 1
        
#     return answer

def solution(skill, skill_trees):
    answer = 0
    
    for sk in skill_trees:
        skillList = ''
        for x in sk:
            if x in skill:
                skillList += x
        
        if skillList == skill[:len(skillList)]:
            answer += 1
        
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))