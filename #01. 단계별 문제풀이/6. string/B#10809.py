Word = input()
Word = list(str(Word))
Alp = [-1]*26

# a = 97 ~ (- 97)
for i in range (len(Word)):
    index = ord(Word[i]) - 97 
    if(Alp[index] == -1):
        Alp[index] = i

for i in range (len(Alp)):
    print(Alp[i], end = ' ')

# 규호형
'''
S = input()

for i, index in enumerate(S):
    print(i, index)**
S = input()

for i, index in enumerate(S):
    print(i, index)
'''

# 승현이
'''
def check(l:list):
    for i in range(97,123):
        if chr(i) in l:
            print(l.index(chr(i)), end=' ')

        else:
            print("-1",end=' ')

if name=="main":
    S = list(input())
    check(S)
'''

# 민준이
'''
string = input()

for i in range(97,123):
    print(string.find(chr(i)), end=" ")
'''