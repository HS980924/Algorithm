def Hanoi_Top(n, start, end):
    if n == 1 :
        print(start, end)
        return
       
    Hanoi_Top(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    Hanoi_Top(n-1, 6-start-end, end) # 3단계

if __name__ == "__main__":
    N = int(input())
    print(2**N-1)
    Hanoi_Top(N,1,3)





