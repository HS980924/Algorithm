def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = i
    
    for i in range(len(discount)-9):
        cnt = [0]*len(want)
        for j in range(i,i+10):
            if discount[j] in dic:
                cnt[dic[discount[j]]] += 1
            else:
                break
        
        if number == cnt:
            answer += 1
    
    return answer

want = ["apple"]
number = 	[10]
discount = 	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
print(solution(want, number, discount))