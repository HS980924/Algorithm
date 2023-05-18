if __name__ == "__main__":
    N = int(input())

    arr = list(map(int, input().split()))

    count = [0 for _ in range(N)]
    '''
    for i in range(N):
        for j in range(i):
            if arr[i]>arr[j] :
                if count[i]<count[j]:
                    count[i] = count[j]
        count[i]+=1

    print(max(count))
    '''

    sk = 1
    for i in range(N):
        for j in range(sk):
            arr[j]
