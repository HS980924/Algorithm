num = int(input())

for i in range(1,num+1):
    print(" "*(num-i) + "*"*i)
    #print(" "*(num-i),"*"*i) ,(콤마)로 문자열을 나열할 경우 공백이 자동으로 추가된다.

#규호형
'''
N = int(input())
i = 0
j = 0

for i in range(N, 0, -1):
    print(" "*(i-1), end="")
    for j in range(N-i+1):
        print("*", end="")
    print(" ")
'''