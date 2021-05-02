sum = 1
num = [int(input()) for _ in range (3)]
for i in range (0,3):
    sum *= num[i]
'''
arr = [0]*9
for i in range (0,9):
    arr[i] = int(input())

''' # 리스트에 입력하는 방법 #기본
sum = list(str(sum))        # 리스트로 변형하는 것
sum = list(map(int,sum))    # 리스트를 정수로 다시 변형


for i in range (0,10):
    count = 0;
    for j in range (len(sum)):
        if sum[j] == i:
            count += 1
    print(count)

'''
for i in range (0,10):
    print(sum.count(i))     
'''

# 승현이 코드
'''
A = int(input())*int(input())*int(input())
for i in range(10):
    print(list(str(A)).count(str(i)))
'''
# 재훈이 코드
'''
A = int(input())
B = int(input())
C = int(input())

tmp = list(str(ABC))

for i in range(10):
    print(tmp.count(str(i)))
'''
