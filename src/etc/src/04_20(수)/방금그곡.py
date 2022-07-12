def timecalc(time1, time2):
    time1 = time1.split(':')
    time2 = time2.split(':')
    
    t1 = int(time1[0]) * 60 + int(time1[1])
    t2 = int(time2[0]) * 60 + int(time2[1])
    
    return t2 - t1

def trans(music):
    result = ""
    i = 0
    while i < len(music)-1:
        if music[i+1] == '#':
            result += str(music[i]).lower()
            i += 1
        else:
            result += music[i]
        i += 1
    
    if music[-1] != '#':
        result += music[-1]
    
    return result
    

def solution(m, musicinfos):
    answer = ''
    result = {}
    compare = {}
    m = trans(m)
    
    for info in musicinfos:
        tmp = info.split(',')        
        diff_time = timecalc(tmp[0],tmp[1])
        musicSyll = trans(tmp[3])
        cnt = 0
        syllable = ""
        
        while cnt < diff_time:
            index = cnt%len(musicSyll)
            syllable += musicSyll[index]
            cnt += 1
            
        compare[tmp[2]] = [syllable,diff_time]
        
    for k, v in compare.items():
        if m in v[0]:
            result[k] = v[1]
    
    
    if not result:
        return '(None)'
    else:
        answer = max(result, key=result.get)
        return answer


m = "CC#BCC#BCC#BCC#B"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m,musicinfos))
