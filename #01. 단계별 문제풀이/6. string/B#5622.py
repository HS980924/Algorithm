#1 -> 2초 이상부터 +1
#단어를 주어졌을 때 최소 시간
Word = list(input())
s = 0

for i in range (len(Word)):
    k = ord(Word[i])
    if (k == ord('S') or k == ord('V') or k == ord('Y') or k == ord('Z')):
        t = (k-65)//3 + 3 - 1
    else:
        t = (k-65)//3 + 3
    s = s + t

print(s)
 



