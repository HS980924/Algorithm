def Fibonachi(N: int):
    if(N <= 1):
        return N
    else:
        return Fibonachi(N-1) + Fibonachi(N-2)

if __name__ == "__main__":
    Num = int(input())
    fibo = Fibonachi(Num)
    print(fibo)