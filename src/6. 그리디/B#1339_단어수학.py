N = int(input())
words = []
dic = {}

for _ in range(N):
    word = list(input())
    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = 10**(len(word)-(i+1))
        else:
            dic[word[i]] += 10**(len(word)-(i+1))

sortedDic = sorted(dic.values(), reverse=True)

answer = 0
num = 9
for value in sortedDic:
    answer += value*num
    num -= 1

print(answer)

# 참고 링크 : https://yoonsang-it.tistory.com/41