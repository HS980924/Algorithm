num1, num2 = input().split()


num1 = list(map(int,num1))
num2 = list(map(int,num2))

num1.reverse()
num2.reverse()

if(num1 > num2):
    for i in range (len(num1)):
        print(num1[i], end = '')
else:
    for i in range (len(num2)):
        print(num2[i], end = '')


#병근
'''
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
if a > b :
    print(a)
else :
    print(b)
'''