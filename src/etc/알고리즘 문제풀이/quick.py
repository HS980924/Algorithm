def solution(s):
    answer = ''
    tmp = list(s)
    sort_tmp = quick(tmp,0,len(tmp)-1)
    
    for i in sort_tmp:
        answer += i
    
    return answer

def quick(tmp,start,end):
    left = start
    right = end
    pivot = (left + right) // 2
    
    while left < right:
        while ord(tmp[left]) > ord(tmp[pivot]):
            left += 1

        while ord(tmp[right]) < ord(tmp[pivot]):
            right -= 1
        
        if left < right:
            tmp[left], tmp[right] = tmp[right], tmp[left]
            print(tmp)
            left += 1
            right -= 1

    if left > right:
        tmp_left = quick(tmp,start,right)
        tmp_right = quick(tmp,left,end)
        return tmp_left + tmp_right

    else:
        return tmp[start:end+1]

#print(solution(S))