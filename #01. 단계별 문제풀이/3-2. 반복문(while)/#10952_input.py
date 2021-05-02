T = True

while T:
    num1, num2 = map(int,input().split())
    if num1 != 0 or num2 != 0:
        print(num1+num2)
    else:
        T = False




