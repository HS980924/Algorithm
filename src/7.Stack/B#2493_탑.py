# Upload BOJ Gold-5 Stack 2493번 탑
# 일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고
# 각 탑의 꼭대기에 레이저 송신기를 설치
# 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사
# 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능
# ex) 6, 9, 5, 7, 4인 다섯 개의 탑 존재
# 동시에 왼쪽 방향으로 레이저 발사


N = int(input())
razer = list(map(int,input().split()))
stack = []
answer = [0]*N

for i in range(N-1, -1, -1):
    while stack and stack[-1][0] <= razer[i]:
        razer_info = stack.pop()
        answer[razer_info[1]] = i+1
    stack.append([razer[i],i]);

# while stack:
#     razer_info = stack.pop()
#     answer[razer_info[1]] = 0

print(*answer)
