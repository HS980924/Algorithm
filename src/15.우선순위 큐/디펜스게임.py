from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    heap = []
    sumEnemy = 0
    
    for value in enemy:
        heappush(heap,-value)
        sumEnemy += value
        
        if sumEnemy > n:
            if k == 0:
                break
            sumEnemy += heappop(heap)
            k -= 1
        answer += 1
        
    return answer
    

n = 7
k = 3 
enemy = [4, 2, 4, 5, 3, 3, 1]
print(solution(n,k,enemy))