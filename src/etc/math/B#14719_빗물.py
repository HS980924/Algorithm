# Upload BOJ Gold-5 implement 15719번 빗물
# 참고 링크 : https://seongonion.tistory.com/115
H, W = map(int,input().split())
heights = list(map(int,input().split()))
answer = 0

for i in range(1,W-1):
    left_max_height = max(heights[:i])
    right_max_height = max(heights[i+1:])
    
    min_height = min(left_max_height, right_max_height)
    
    if heights[i] < min_height:
        answer += min_height-heights[i]

print(answer)
