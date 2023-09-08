# 2022.07.25 (월)
# 숫자 블록 - ???
# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/12923

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1) 
        for j in range(2, int(i**0.5)+1):
            if i%j == 0 and i//j <= 10000000:
                k = i//j
                break
        answer.append(k)
    
    return answer

begin, end = 1,10
print(solution(begin,end))