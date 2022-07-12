def solution(word):
    alpa = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    answer = len(word)
    loop = (((5+1)*5+1)*5+1)*5+1 # 781
    
    for x in word:
        answer += loop*alpa[x]
        loop = (loop-1) // 5
        
    return answer

word = ["AAAAE","I", "EIO"]

for x in word:
    print(solution(x))
    
##########################다른 방법#############################
