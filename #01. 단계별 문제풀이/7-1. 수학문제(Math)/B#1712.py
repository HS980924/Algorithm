# A = 고정 지출 비용
# B = 재료비와 인건비 등 가변 비용
# A + B = 노트북 한대 생산 비용
# A + 10B = 노트북 10대 생산 비용
# C =  C만원(노트북 가격)
# 손익 분기점 출력 but 없으면 -1 출력
import math

A, B, C = map(int,input().split())

con = 0
if(C>B):
    con = math.ceil(A/(C-B))
    if(A % (C-B) == 0):
        con += 1
else:
    con = -1

print(con)

