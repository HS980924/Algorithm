# 높이 V인 나무 막대
# 낮에 A미터 올라갈수 있다
# 밤을 자는 동안 B미터 미끄러진다
# 또 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면 며칠이 걸리는가?

# v <= (A-B)*d
import math
d = 0
A, B, V = map(int,input().split())

d = (V-B)/(A-B)

print(math.ceil(d))

'''
print(int((C-B)/(A-B))) if (C+B)%(A-B) == 0 else print(int((C-B)/(A-B))+1)
'''