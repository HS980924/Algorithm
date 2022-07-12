def solution(people, limit):
    answer = 0
    people.sort()
    
    while people:
        tmp = 0
        tmp += people.pop()
        while people != [] and tmp + people[0] <= limit:
            tmp += people.pop(0)
        
        answer += 1
        
    return answer

def solution(people, limit):
    answer = 0
    left = 0
    right = len(people)-1
    people.sort()
    
    while left <= right:
        tmp = 0
        tmp += people[right]
        while tmp + people[left] <= limit:
            tmp += people[left]
            left += 1
        right -= 1
        answer += 1
        
    return answer

p = [70, 50, 80, 50]
li = 100

print(solution(p,li))