Ham = []
drink = []
for i in range(3):
    Ham.append(int(input()))
for i in range(2):
    drink.append(int(input()))

MIN = min(Ham) + min(drink) - 50

print(MIN)
