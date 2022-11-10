def solution(a, b, n):
    answer = 0
    while n > (a-1):
        cnt = (n // a)*b
        answer += (n // a)*b
        n = cnt + n%a
    return answer

print(solution(2,1,20))