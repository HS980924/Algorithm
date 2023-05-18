from heapq import heappush, heappop
def solution(operations):
    answer = []
    maxHeap = []
    minHeap = []
    visited = []
    i = 0
    
    for oper in operations:
        op = oper.split()
        if op[0] == "I":
            heappush(minHeap,(int(op[1]), i))
            heappush(maxHeap,(int(op[1])*-1, i))
            visited.append(False)
            i += 1
        else:
            if minHeap and op[1] == "-1":
                value = heappop(minHeap)
                visited[value[1]] = True
            if maxHeap and op[1] == "1":
                value = heappop(maxHeap)
                visited[value[1]] = True
                
        while minHeap and visited[minHeap[0][1]]:
            heappop(minHeap)
        while maxHeap and visited[maxHeap[0][1]]:
            heappop(maxHeap)
    
    if not minHeap:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(maxHeap[0][0]*-1)
        answer.append(minHeap[0][0])
    
    return answer
