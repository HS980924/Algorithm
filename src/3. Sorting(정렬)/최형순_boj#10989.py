'''
if __name__ == "__main__":
    N = int(input())
    Num = []

    for i in range(N):
        Num.append(int(input()))

    countSum = [0]*(max(Num)+1)

    for i in range(0,max(Num)+1):
        if i > 0:
            countSum[i] = countSum[i-1] + Num.count(i)
        else:
            countSum[i] = Num.count(i)

    arr = [0]*(N+1)

    for i in range(N-1,-1,-1):
        arr[countSum[Num[i]]] = Num[i]
        countSum[Num[i]] -= 1
    
    for i in range(1,N+1):
        print(arr[i])
'''
import sys

if __name__ == "__main__":
    N = int(input())
    count = [0]*10001
    
    for i in range(N):
        count[int(sys.stdin.readline())] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i)

    


    
        
