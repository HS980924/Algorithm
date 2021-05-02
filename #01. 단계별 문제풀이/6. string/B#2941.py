
Word = input()
a = []

if 'c=' in Word:
    Word = Word.replace('c=',"1")
if 'c-' in Word:
    Word = Word.replace('c-',"1")
if 'dz=' in Word:
    Word = Word.replace('dz=',"1")
if 'd-' in Word:
    Word = Word.replace('d-',"1")
if 'lj' in Word:
    Word = Word.replace('lj',"1")
if 'nj' in Word:
    Word = Word.replace('nj',"1")
if 's=' in Word:
    Word = Word.replace('s=',"1")
if 'z=' in Word:
    Word = Word.replace('z=',"1")

print(len(Word))

# 민준
'''
string = input()
tmp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in tmp:
    string = string.replace(i, "1")

print(len(string))
'''
# 병근
'''
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳 리스트
s = input() # 문자열을 입력받아 s에 저장
for i in croatia: # 크로아티아 문자 하나씩 검사
    s = s.replace(i,'a') # s에 크로아티아 문자가 있으면 a로 변경
print(len(s)) # s의 길이 측정 = s의 알파벳 갯수
'''

#승현
'''
S = list(input())
count = 0
S.append('\0')
for i in range(0,len(S)-1):
    if(ord(S[i])>=97 and ord(S[i])<=122):
        if (S[i+1] == '=') or (S[i+1] == '-'):
            count -= 1
        if S[i] == 'd' and S[i+1] == 'z' :
            if S[i+2]=='=':
                count -= 1
        if S[i] == 'l' and S[i+1] == 'j':
            count -= 1
        if S[i] == 'n' and S[i+1] == 'j':
            count -= 1

    count += 1
print(count)
'''