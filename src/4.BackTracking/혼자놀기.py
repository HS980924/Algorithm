def solution(cards):
    answer = dfs(cards)
    return answer

def getCardGroup(cards, idx, check):
    cnt = 0    
    while check[idx]:
        check[idx] = False
        idx = cards[idx] -1
        cnt += 1
    
    return cnt

def dfs(cards):
    answer = 0
    for i in range(len(cards)):
        check = [True]*len(cards)
        group1 = getCardGroup(cards,i,check)
        
        for j in range(i+1,len(cards)):
            group2 = getCardGroup(cards,j, check)
            answer = max(group1 * group2, answer)
    
    return answer

cards = [8,6,3,7,2,5,1,4]
print(solution(cards))