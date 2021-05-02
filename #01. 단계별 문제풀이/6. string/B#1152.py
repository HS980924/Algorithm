#1. 문자열을 공백 기준으로 리스트로 재설정할 수 있지 않을까?
#2. 공백 개수 + 1 but 앞 뒤에 있을 경우 공백 개수만큼
enter = list(input())

count = 0
count = enter.count(' ') + 1
if(enter[0] == ' '):
    count = count - 1
if(enter[len(enter)-1] == ' '):
    count = count - 1

print(count)

# 규호형
'''
enter = input()
enter = enter.strip().split()
print(len(enter))
'''

