Test_case = int(input())


for i in range (Test_case):
    num ,Word = input().split()
    num = int(num)
    Word = list(str(Word))
    
    for i in range (len(Word)):
        for j in range (num):
            print(Word[i], end = '')
    print(end = '\n')
    
# 승현이
'''
T = int(input())
for i in range(T):
    S = list(input())
    for j in range(2,len(S)):
        for k in range(int(S[0])):
            print(S[j], end='')
    print()
'''

# 병근이
'''
C = int(input("Test Case : "))
for i in range(C):
    N, T = input().split()
    moonja = ""
    for i in T:
        moonja = moonja + int(N)*i
    print(moonja)
'''

# 민준이
'''
T = int(input())
tmp = ""

for i in range(T):
    Num,S = input().split()
    for j in S:
        print(j*int(Num), end="")
    print()
'''