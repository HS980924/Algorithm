A,B = input().split()

A = list(map(int,A))
B = list(map(int,B))

C = []
y = 0

A.reverse()
B.reverse()

if(len(A) > len(B)):
    max = len(A)
    s = len(A)-len(B)
    B.extend(s*[0])
else:
    max = len(B)
    s = len(B)-len(A)
    A.extend(s*[0])


for i in range (max):
    x = (A[i] + B[i] + y) % 10                  #일의 자리
    C.append(x)
    y = (A[i] + B[i] + y) // 10                 #십의 자리

if(y == 1):
    C.append(y)

C.reverse()
for i in range (len(C)):
    print(C[i], end = "")

'''
A, B = map(int,input().split())
print(A+B)
'''
# 파이썬3 에서는 산술 오버플로우 존재 x
# 라이브러리 사용시 c기반인게 있어 스택 오버플로우 발생 o