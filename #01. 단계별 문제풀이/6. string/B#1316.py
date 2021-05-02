'''
Num = int(input())
count = 0
for i in range (Num):
    b = list(input())
    statue = 1
    for i in range (len(b)-1):
        if b[i] == b[i+1]:
            status = 1
            continue
        else:
            if b[i] in b[i+1:len(b)]:
                statue = 0
                break
    if(statue == 1):
        count += 1
    
print(count)
'''

def check(S:list):
    B =[]
    S.append('\0')
    for i in range(0,len(S)-1):
        if S[i]!=S[i+1]:
            if S[i] in B:
                return 0
            else:
                B.append(S[i])
    return 1
    
if __name__ =="__main__":
    N = int(input())
    count = 0
    for i in range(N):
        S = list(input())
        count+= check(S)
    print(count)

# 병근
'''
a, b = 0, 0
N = int(input())
for i in range(N):
    S = input().lower()
    for j in range(1, len(S)):
        a = S.find(S[j-1])
        b = S.find(S[j])
        if a > b:
            N -= 1
            break
print(N)
'''

# 승현
'''
def check(S:list):
    B =[]
    S.append('\0')
    for i in range(0,len(S)-1):
        if S[i]!=S[i+1]:
            if S[i] in B:
                return 0
            if S[i] not in B:
                B.append(S[i])
    return 1

if name =="main":
    N = int(input())
    count = 0
    for i in range(N):
        S = list(input())
        count+= check(S)
    print(count)
'''

# 민준
'''
count = 0
num = int(input())

for i in range(num):
    string = input()
    if list(string) == sorted(string, key=string.find):
        count += 1

print(count)
'''