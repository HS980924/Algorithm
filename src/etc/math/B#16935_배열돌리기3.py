# Upload BOJ Gold-5 implement 16935번 배열 돌리기3
N, M, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
operation = list(map(int,input().split()))

for oper in operation:
    N = len(arr)
    M = len(arr[0])
    if oper == 1:
        # 상하 반전
        for i in range(N//2):
            for j in range(M):
                tmp = arr[i][j]
                arr[i][j] = arr[N-1-i][j]
                arr[N-1-i][j] = tmp
    elif oper == 2:
        # 좌우 반전
        for i in range(N):
            for j in range(M//2):
                tmp = arr[i][j]
                arr[i][j] = arr[i][M-1-j]
                arr[i][M-1-j] = tmp
    elif oper == 3:
        # 오른쪽 90도 회전
        answer = []
        for j in range(M):
            tmp = []
            for i in range(N):
                tmp.append(arr[N-1-i][j])
            answer.append(tmp)
        arr = answer.copy()
    elif oper == 4:
        # 왼쪽 90도 회전
        answer = []
        for j in range(M):
            tmp = []
            for i in range(N):
                tmp.append(arr[i][M-1-j])
            answer.append(tmp)
        arr = answer.copy()
    elif oper == 5:
        # 부분 배열 오른쪽 이동
        answer = []
        for i in range(N//2):
            tmp = []
            for j in range(M//2):
                tmp.append(arr[N//2+i][j])
            for j in range(M//2):
                tmp.append(arr[i][j])
            answer.append(tmp)
        for i in range(N//2,N):
            tmp = []
            for j in range(M//2,M):
                tmp.append(arr[i][j])
            for j in range(M//2,M):
                tmp.append(arr[i-(N//2)][j])
            answer.append(tmp)
        arr = answer.copy()
    else: 
        # 부분 배열 왼쪽 이동
        answer = []
        for i in range(N//2):
            tmp = []
            for j in range(M//2,M):
                tmp.append(arr[i][j])
            for j in range(M//2,M):
                tmp.append(arr[i+(N//2)][j])
            answer.append(tmp)
        for i in range(N//2):
            tmp = []
            for j in range(M//2):
                tmp.append(arr[i][j])
            for j in range(M//2):
                tmp.append(arr[i+(N//2)][j])
            answer.append(tmp)
        arr = answer.copy()
    
for i in range(len(arr)):
    print(*arr[i])