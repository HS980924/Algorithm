a = input()
a = int(a)

if a <= 100 and a >= 90:
    print("A")
elif a < 90 and a >= 80:
    print("B")
elif a < 80 and a >= 70:
    print("C")
elif a < 70 and a >= 60:
    print("D")
else:
    print("F")