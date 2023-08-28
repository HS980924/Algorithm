# Upload BOJ Gold-4 Heap 7662번 이중우선순위큐
import sys
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    max_queue = []
    min_queue = []
    delete = [False]*(k)
    cnt = 0
    for i in range(k):
        exp, num = map(str,input().split())
        if exp == "I":
            # 큐에 삽입
            heapq.heappush(max_queue,[-int(num),i])
            heapq.heappush(min_queue,[int(num),i])
            cnt += 1
        else:
            # 큐에서 삭제
            if cnt:
                if int(num) < 0:
                    # 최솟값 삭제
                    while delete[min_queue[0][1]]:
                        heapq.heappop(min_queue)
                    popData = heapq.heappop(min_queue)
                    delete[popData[1]] = True
                else:
                    # 최댓값 삭제
                    while delete[max_queue[0][1]]:
                        heapq.heappop(max_queue)
                    popData = heapq.heappop(max_queue)
                    delete[popData[1]] = True
                cnt -= 1
                
    while min_queue and delete[min_queue[0][1]]:
            heapq.heappop(min_queue)
            
    while max_queue and delete[max_queue[0][1]]:
        heapq.heappop(max_queue)
        
    if cnt:
        # 최댓값 최솟값 출력
        print(-max_queue[0][0], min_queue[0][0])
    else:
        print("EMPTY")