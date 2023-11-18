# Upload BOJ Silver-1 Heap 1713번 후보 추천하기
import heapq
N = int(input())
recommend = int(input())
recommendList = list(map(int,input().split()))
heap = []

for i in range(len(recommendList)):
    num = recommendList[i]
    tmp_list = []
    check = False
    
    while heap:
        cnt, time, std_num = heapq.heappop(heap)
        if std_num == num:
            check = True
            cnt += 1
        heapq.heappush(tmp_list,[cnt,time,std_num])
    
    if not check and len(tmp_list) >= N:
        heapq.heappop(tmp_list)
    
    if not check and len(tmp_list) < N:
        heapq.heappush(tmp_list,[1,i,num])
        
    heap = tmp_list

answer = [ x[-1] for x in heap ]
answer.sort()
print(*answer)