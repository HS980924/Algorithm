def solution(msg):
    alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = []
    arr = []
    i = 0
    for x in alpa:
        arr.append(x)
    
    while i < len(msg):
        tmp = msg[i]
        while tmp in arr:
            i += 1
            if i < len(msg):
                tmp += msg[i]
            else:
                break
        if tmp not in arr:
            arr.append(tmp)
            answer.append(arr.index(tmp[:-1])+1)
        else:
            answer.append(arr.index(tmp)+1)
    print(arr)    
    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))