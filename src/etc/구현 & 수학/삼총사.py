def solution(number):
    answer = recur(0,0,number)
    return answer

def recur(result,n,number):
    if n == 3:
        if result == 0:
            return 1
        return 0
    else:
        cnt = 0
        for idx in range(len(number)):
            cnt += recur(result+number[idx],n+1,number[idx+1:])
        return cnt