def solution(s):
    answer = [0,0]
    
    while s != '1':
        cnt = s.count('0')
        tranS = s.replace('0','')
        s = bin(len(tranS))
        s = s[2:]
        answer[0] += 1
        answer[1] += cnt
        
    return answer


s = "1111111"
print(solution(s))