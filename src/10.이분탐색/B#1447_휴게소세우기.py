# Upload BOJ Gold-4 BinarySearch 휴게소세우기

# import heapq

# N, M, L = map(int, input().split())
# hugeso = list(map(int, input().split()))
# hugeso.append(0)
# hugeso.append(L)
# hugeso.sort()
# heap = []
# cnt = 0
# print(hugeso)

# for i in range(1,N+2):
#     distance = hugeso[i] - hugeso[i-1]
#     heapq.heappush(heap,(-distance,hugeso[i-1],hugeso[i]))

# while M > cnt:
#     cnt += 1
#     distance, start, end = heapq.heappop(heap)
#     distance2 = (distance*-1)//2
#     mid = start+distance2
#     heapq.heappush(heap,(-(mid-start),start,mid))
#     heapq.heappush(heap,(-(end-mid),mid,end))
#     print(cnt, heap)

# print(-heap[0][0])


#############################################################
# 참고 링크 : https://olive-su.tistory.com/m/292
# 문제를 잘못 이해헀음
# M개의 휴게소를 한번에 배치를 해야함
N, M, L = map(int, input().split())
hugeso = list(map(int, input().split()))
hugeso.append(0)
hugeso.append(L)
hugeso.sort()

start = 1
end = L
ans = 0
while start <= end:
    cnt = 0
    mid = (start+end)//2
    
    for i in range(len(hugeso)-1):
        if hugeso[i+1]-hugeso[i] > mid:
            cnt += ((hugeso[i+1]-hugeso[i])-1)//mid
    
    if cnt > M:
        start = mid+1
    else:
        ans = mid
        end = mid-1

print(ans)