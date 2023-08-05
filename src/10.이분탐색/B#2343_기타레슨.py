# Upload BOJ Silver-1 BinarySearch 2343번 기타레슨

# 총 N개의 강의, 블루레이를 녹화할 때, 강의의 순서가 바뀌면 안됨
# 즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화
# 해당 블루레이의 개수를 가급적 줄이려고 함
# M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 했다.
# 블루레이의 크기를 최소로 하려고 함
# M개의 블루레이는 모두 같은 크기이어야 함
# 각 강의의 길이가 분 단위로 주어짐, 가능한 블루레이의 크기 중 최소를 구하는 프로그램

N, M = map(int,input().split())
lecture = list(map(int,input().split()))
answer = 0

start = max(lecture)
end = sum(lecture)

while start <= end:
    mid = (start + end)//2
    
    cnt = 0
    bluelay = 0
    
    for i in range(N):
        if bluelay + lecture[i] > mid:
            bluelay = 0
            cnt += 1
        bluelay += lecture[i]
        
    if bluelay:
        cnt += 1
            
    if cnt > M:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
        
print(answer)