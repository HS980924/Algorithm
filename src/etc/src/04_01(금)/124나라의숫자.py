def third(N):
    arr = [4,1,2]
    result = ""
    while N > 0:
        result += str(arr[N%3])
        if N%3 == 0:
            N = N//3 -1
        else:
            N = N//3
    
    return result[::-1]

def solution(n):
    answer = ''
    answer = third(n)
    return answer