# 오큰수

import sys
N = int(sys.stdin.readline())
suyul = list(map(int,sys.stdin.readline().split()))
answer = [-1]*N
stack = [0]

for i in range(1,N):
    while stack and suyul[stack[-1]] < suyul[i]:
        answer[stack.pop()] = suyul[i]
    stack.append(i)
    
print(*answer)




# 리스트 출력 시 * 기호 사용하면 깔끔하게 출력됨
# 참고 링크
# https://hooongs.tistory.com/329 (그림 & 원리)
# https://hongcoding.tistory.com/40 ( 코드 )