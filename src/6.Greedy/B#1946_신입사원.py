# Upload BOJ Silver-1 Greedy 신입사원
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    person = []
    for i in range(N):
        score1, score2 = map(int, input().split())
        person.append([score1,score2])
        
    person.sort()
    cnt = 0
    scr1 = N
    scr2 = N
    for i in range(N):
        if scr1 > person[i][0] or scr2 > person[i][1]:
            cnt += 1
            scr1 = min(scr1, person[i][0])
            scr2 = min(scr2, person[i][1])

    print(cnt)

    
    # 1번째 1, 4
    # 범위 (1, 4)
    # 2번째 4, 2
    # 범위 (4, 4)
    # 3번째 2, 5
    # 4번째 6, 1
    # 범위 (6, 4)
    
    # 3, 3
    # 1, 6
    # 
    
    
    
    
