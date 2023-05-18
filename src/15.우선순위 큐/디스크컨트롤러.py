from heapq import heappop, heappush
def solution(jobs):
    answer = 0
    nowTime = 0
    start = -1
    jobCnt = 0
    heap = []
    
    while jobCnt < len(jobs):
        for j in jobs:
            if start < j[0] <= nowTime:
                heappush(heap,(j[1],j[0]))
        if len(heap) > 0:
            job = heappop(heap)
            start = nowTime
            nowTime += job[0]
            answer += nowTime - job[1]
            jobCnt += 1
        else:
            nowTime += 1
    
    return answer // len(jobs)

jobs = [[0, 1], [0, 1], [0, 1]]
print(solution(jobs))