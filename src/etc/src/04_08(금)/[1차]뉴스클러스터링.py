def transStr(str3):
    result = []
    for i in range(len(str3)-1):
        tmp = str(str3[i]+str3[i+1])
        if tmp.isalpha():
            result.append(tmp.lower())
    #print(result)
    return result

def intersection(str1,str2):
    result = 0
    if str1 == [] and str2 == []:
        result = 1
    else:
        tmp1 = list(set(str1+str2))
        for word in tmp1:
            cnt1 = str1.count(word)
            cnt2 = str2.count(word)
            result += min(cnt1,cnt2)
    return result

def union(str1,str2):
    result = 0
    if str1 == [] and str2 == []:
        result = 1
    else:
        tmp1 = list(set(str1+str2))
        for word in tmp1:
            cnt1 = str1.count(word)
            cnt2 = str2.count(word)
            result += max(cnt1,cnt2)
                
    return result
                
def solution(str1, str2):
    answer = 0
    st1 = transStr(str1)
    st2 = transStr(str2)
    
    INTERSEC = intersection(st1,st2)
    UNION = union(st1,st2)
    print(INTERSEC,UNION)
    answer = int((INTERSEC/UNION)*65536)
    
    return answer

str1 = 'FRANCE'
str2 = 'french'
print(solution(str1,str2))