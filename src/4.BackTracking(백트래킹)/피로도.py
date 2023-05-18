def solution(k, dungeons):
    answer = -1
    global check_route
    check_route = [True]*len(dungeons)
    answer = dfs(k,dungeons,0)
    return answer

def dfs(k, dungeons, cnt):
    answer = cnt
    for i in range(len(dungeons)):
        if check_route[i] and dungeons[i][0] <= k:
            check_route[i] = False
            answer = max(dfs(k-dungeons[i][1],dungeons,cnt+1),answer)
            check_route[i] = True    
            
    return answer
    



k = 80
dungeonss = [[80,20],[50,40],[30,10]]

print(solution(k,dungeonss))