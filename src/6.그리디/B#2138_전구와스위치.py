# Upload BOJ Gold-5 Greedy 전구와스위치
# 참고링크 : https://javaiyagi.tistory.com/593
N = int(input())
now = list(input())
target = list(input())

def change_zero(light):
    cnt = 1
    light[0] = str(1-int(light[0]))
    light[1] = str(1-int(light[1]))
    
    for i in range(1,N):
        if light[i-1] == target[i-1]:
            continue
        else:
            cnt +=1
            light[i-1] = str(1-int(light[i-1]))
            light[i] = str(1-int(light[i]))
            if i+1 < N:
                light[i+1] = str(1-int(light[i+1]))
                
    if light == target:
        return cnt
    
    return N+2

def non_change_zero(light):
    cnt = 0
    
    for i in range(1,N):
        if light[i-1] == target[i-1]:
            continue
        else:
            cnt +=1
            light[i-1] = str(1-int(light[i-1]))
            light[i] = str(1-int(light[i]))
            if i+1 < N:
                light[i+1] = str(1-int(light[i+1]))
                
    if light == target:
        return cnt
    
    return N+2

answer = min(change_zero(now[:]), non_change_zero(now[:]))

if answer == N+2:
    answer = -1
print(answer)