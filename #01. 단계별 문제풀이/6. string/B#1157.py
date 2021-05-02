Word = input()
Word = list(Word.upper())
copy = list(set(Word))

cnt = []
MAX = 0
index = 0
num = 0

for i in range (len(copy)):
    num = Word.count(copy[i])
    if num > MAX:
        index = i
        MAX = num
    elif num == MAX:
        index = -1

if index == -1:
    print("?")
else: print(copy[index])