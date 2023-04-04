from itertools import product

def solution(users, emoticons):
    answer = []
    discontInfo = product([10,20,30,40], repeat=len(emoticons))

    for Info in discontInfo:
        tmp = [0]*len(users)
        for i in range(len(Info)):
            cost = int(emoticons[i] - (Info[i] / 100)*emoticons[i])
            for j in range(len(users)):
                if users[j][0] <= Info[i]:
                    tmp[j] += cost
        cnt = 0
        cost = 0
        for i in range(len(users)):
            if tmp[i] >= users[i][1]:
                cnt += 1
            else:
                cost += tmp[i]
        answer.append([cnt,cost])
    answer.sort(key=lambda x: (-x[0],-x[1]))

    return answer[0]
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users,emoticons))