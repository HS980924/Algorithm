# 2022.08.15(월)
# <B#2110> 공유기설치 - 이분탐색
# 참고링크 : https://www.acmicpc.net/problem/2110

import sys

N, C = map(int,input().split())
home = [ int(sys.stdin.readline()) for _ in range(N)]
home.sort()

def binary_search():
    start, end = 1, home[-1]-home[0]
    result = 1
    
    while start <= end:
        mid = (start + end) // 2     # 공유기 거리
        current = home[0]
        cnt = 1
        
        for i in range(1,N):
            if home[i] >= current + mid:
                current = home[i]
                cnt += 1
                
        if cnt < C:
            end = mid-1
        else:
            result = mid
            start = mid + 1
    
    return result

print(binary_search())