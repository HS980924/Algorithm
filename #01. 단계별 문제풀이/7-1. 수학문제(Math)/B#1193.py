Num = int(input())

i = 1
while(Num > i):
    Num -= i
    i += 1

if( i % 2 == 0):
    Bunmo = i
    Bunja = 1
else:
    Bunmo = 1
    Bunja = i
       

while(Num > 1):
    if( i % 2 == 0):
        Bunja += 1
        Bunmo -= 1
    else:
        Bunja -= 1
        Bunmo += 1
    Num -= 1

print(str(Bunja)+"/"+str(Bunmo))

'''
Num = int(input())

i = 1
while(Num > i):
    Num -= i
    i += 1

if( i % 2 == 0):
    Bunmo = i - Num + 1
    Bunja = Num
else:
    Bunmo = Num
    Bunja = i - Num + 1

print(str(Bunja)+"/"+str(Bunmo))
'''