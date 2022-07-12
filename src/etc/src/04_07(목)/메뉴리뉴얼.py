import itertools

def solution(orders, course):
    answer = []
    for i in course:
        dic = {}
        for order in orders:
            list1 = list(map(list,itertools.combinations(sorted(order),i)))
            for x in list1:
                food = "".join(x)
                if food in dic:
                    dic[food] += 1
                else:
                    dic[food] = 1
        tmp = []
        for key, value in dic.items():
            if max(dic.values()) == value and value > 1:
                tmp.append(key)
        answer += tmp

    answer.sort()
    return answer

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders,course))