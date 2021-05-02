def factorial(N:int):
    if(N == 1 or N == 0):
        return 1
    else:
        return N*factorial(N-1)
#nCr = n! / (r!*(n-r)!)
def Combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

#nPr = n! / (n-r)!
def Permutation(n, r):
    return factorial(n) / factorial(n-r)

if __name__ == "__main__":
    N = int(input())
    R = int(input())
    print(factorial(N))
    print(Combination(N,R))
    print(Permutation(N,R))
