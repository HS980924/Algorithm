T = int(input())
# 1. 리스트
# 2. 수식

for i in range (T):
    k = int(input())    # 층    k층 n호
    n = int(input())    # 호
    matrix =  [[0 for col in range(n)] for row in range(k+1)]

    for i in range (n):
        matrix[0][i] = i+1

    for i in range (1,k+1):
        for j in range (n):
            matrix[i][j] = sum(matrix[i-1][0:j+1])

    print(matrix[k][n-1])

# 승현이
'''
for i in range(int(input())):
    apt = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], ]
    k = int(input())
    n = int(input())
    for j in range(1,k+1):
        tmplist=[]
        for l in range(n):
            tmplist.append(sum(apt[j-1][:l+1]))
        apt.append(tmplist)
    print(apt[k][n-1])
'''


# 병근이
'''
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    p = []
    for j in range(1,n+1): # 0층에 사는 인간들 리스트에 누적 인구수 넣어놓고
        p.append(j)
    for a in range(k):  # k층 까지 반복
        for b in range(1,n):    # 1호 제외하고 2호부터 n호까지 층마다 누적인구수 다시 넣어놈 
            p[b] = p[b] + p[b-1]
    print(p[n-1]) # 원하는 호에 해당한느 리스트의 값 출력
'''

# 재훈이
'''
T = int(input())

for _ in range(T):
k = int(input())#층
n = int(input())#호
room = [k for k in range(1, n+1)] # 각 층별 인원

for i in range(k):
    for j in range(1, n):
        room[j] += room[j-1]
        #print("{0}층 {1}번째 : {2}, ".format(i+1, j+1, room[j]))
print(room[-1])
'''

# 민준이
'''
T = int(input()) # Test case

for i in range(T):
    k = int(input())
    n = int(input()) # k = 층수 / n = 호수 
    floor0 = [i for i in range(1,n+1)]

    for i in range(k):
        for j in range(1,n): 
            floor0[j] = sum(floor0[j-1:j+1])

    print(floor0[n-1])
'''
