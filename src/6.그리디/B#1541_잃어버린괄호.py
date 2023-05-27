# Upload BOJ Silver-2 Greedy 잃어버린괄호

# def expression(exp):
#     ex = []
#     num = ''
#     for x in exp:
#         if x == '+' or x == '-':
#             ex.append(num)
#             ex.append(x)
#             num = ''
#         else:
#             num += x
    
#     if num:
#         ex.append(num)
        
#     return ex

# exp = expression(input())

# result = 0
# idx = 0
# tmp = 0

# while idx < len(exp):
#     if tmp:
#         if exp[idx] == '-':
#             result -= tmp
#             tmp = 0
#             idx += 1
#             tmp += int(exp[idx])
#         elif exp[idx] != '+':
#             tmp += int(exp[idx])
#     else:
#         if exp[idx] == '-':
#             idx += 1
#             tmp += int(exp[idx])
#         elif exp[idx] != '+':
#             result += int(exp[idx])
#     idx += 1
    
# if tmp:
#     result -= tmp
# print(result)


#################################################################################

exp = input().split('-') #'-'를 기준으로 split해서 exp 리스트에 저장

num = [] #'-'로 나눈 항들의 합을 저장할 리스트

for i in exp:
    sum = 0
    tmp = i.split('+') #덧셈을 하기 위해서 '+'를 기준으로 split
    for j in tmp: #split한 리스트의 각 요소들을 더해줌
        sum += int(j)
    num.append(sum) #각 항의 연산 결과(덧셈)를 num에 저장

n = num[0] #식의 제일 처음은 숫자로 시작하기 때문에 0번째 값에서 나머지 값들을 빼준다

for i in range(1,len(num)): #1번째 값부터 n에서 빼준다
    n -= num[i]
print(n)