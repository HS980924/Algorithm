# Upload BOJ Gold-4 Hash 5052번 전화번호 목록
# 참고 블로그 : https://velog.io/@injoon2019/알고리즘-백준-5052-전화번호-목록-파이썬
# 참고 블로그 : https://alpyrithm.tistory.com/72

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    phone_list = []
    hash = dict()
    
    for _ in range(N):
        phone_list.append(input().rstrip())
        
    phone_list.sort()
    
    success = True
    for phoneNum in phone_list:
        for i in range(len(phoneNum)):
            if phoneNum[:i+1] in hash:
                success = False
                break
        hash[phoneNum] = 1
        if not success:
            break
        
    if success:
        print("YES")
    else:
        print("NO")
    