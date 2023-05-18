def factorial (N:int):
    if(N == 1 or N == 0):
        return 1
    else:
        return N*factorial(N-1)

if __name__ == "__main__":
    Num = int(input())
    fac = factorial(Num)
    print(fac)