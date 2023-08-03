# Upload BOJ Gold-2 BinarySearch 1300번 K번째 수
# N x N 배열 A 만듦
# 배열에 들어있는 수 A[i][j] = i*j
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 N*N이된다.
# B를 오름차순으로 정렬했을 때, B[k]를 구해보자
# 배열 A와 B의 인덱스는 1부터 시작

N = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    mid = (start+end)//2
    
    tmp = 0
    for i in range(1,N+1):
        tmp += min(mid//i,N)
    
    if tmp >= k:
        answer = mid
        end = mid-1
    else:
        start = mid+1
print(answer)