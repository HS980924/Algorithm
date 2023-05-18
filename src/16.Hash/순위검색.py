# # 2022.07.27(수)
# # 순위검색 - >??문제
# # 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/72412

# from collections import deque

# def solution(info, query):
#     answer = []
#     infos = [[] for _ in range(5)]
    
#     for sen in info:
#         tmp = str(sen).split(' ')
#         for i in range(5):
#             infos[i].append(tmp[i])
    
#     for sen in query:
#         tmp = str(sen).replace(' and ',' ')
#         query_list = tmp.split(' ')
#         queue = deque([0,1,2,3,4])
#         for i in range(5):
#             if query_list[i] == '-':
#                 continue
#             else:   
#                 length = len(queue)
#                 for j in range(length):
#                     ind = queue.popleft()
#                     if query_list[i].isdigit():
#                         if int(query_list[i]) <= int(infos[i][ind]):
#                             queue.append(ind)
#                     else:
#                         if query_list[i] == infos[i][ind]:
#                             queue.append(ind)
#         answer.append(len(queue))
    
#     return answer



# info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# print(solution(info,query))

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for sentance in info:
        tmp = sentance.split()
        conditions = tmp[:-1]
        score = int(tmp[-1])
        for i in range(5):
            case = list(combinations(range(4),i))
            for c in case:
                conditionCopy = conditions.copy()
                for idx in c:
                    conditionCopy[idx] = "-"
                key = ''.join(conditionCopy)
                dic[key].append(score)
    
    for value in dic.values():
        value.sort()
    
    for q_value in query:
        tmp = q_value.replace('and ','')
        query_list = tmp.split()
        target_key = ''.join(query_list[:-1])
        target_score = int(query_list[-1])
        cnt = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list,target_score)
            cnt = len(target_list) - idx
        answer.append(cnt)
    
    return answer



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))