# Upload BOJ Silver-2 BinarySearch 1654번 랜선자르기

# N개의 랜선을 만들어야 함
# K개의 랜선을 가지고 있음
# K개의 랜선의 길이가 제각각
# 모두 N개의 같은 길이의 랜선을 만들어야함
# 센티미터 단위로 정수 길이만큼 자른다.
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함
# 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램 작성
import sys
K, N = map(int,input().split())
cables = [ int(input()) for _ in range(K)]

start = 1
end = max(cables)
answer = 0

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for length in cables:
        cnt += length // mid
    
    if cnt >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
    
print(answer)
    
