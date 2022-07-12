def change(Num,div):
    result = []
    if Num == 0:
        return str(0)
    else:
        while Num:
            if Num%div >= 10:
                result.append(chr((Num%div)+55))
            else:
                result.append(str(Num%div))
            Num //= div
        return result[::-1]
    

def solution(n, t, m, p):
    answer = ''
    order = 0
    num = 0
    while len(answer) < t:
        trans_num = change(num,n)
        for i in range(len(trans_num)):
            if order%m == (p-1):
                answer += trans_num[i]
            if len(answer) == t:
                break
            order += 1
        num += 1
        
    return answer