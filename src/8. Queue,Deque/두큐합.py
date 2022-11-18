from collections import deque

def solution(queue1, queue2):
    answer = -1
    queue1Sum = sum(queue1)
    queue2Sum = sum(queue2)
    sameSum = (queue1Sum + queue2Sum) // 2 
    queue1Copy = deque(queue1)
    queue2Copy = deque(queue2)
    cnt = 0
    
    while cnt < len(queue1) * 3:
        if sameSum < queue1Sum:
            value = queue1Copy.popleft()
            queue2Copy.append(value)
            queue1Sum -= value
            queue2Sum += value
        elif sameSum > queue1Sum:
            value = queue2Copy.popleft()
            queue1Copy.append(value)
            queue1Sum += value
            queue2Sum -= value
        else:
            answer = cnt
            break
        cnt += 1
    
    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]	

print(solution(queue1,queue2))