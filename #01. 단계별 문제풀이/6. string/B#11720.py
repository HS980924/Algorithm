count = int(input())

# Num = str(input())
# Num = list(map(int,Num))
Num = list(input())
for i in range (count):
    Num[i] = int(Num[i])

print(sum(Num))


