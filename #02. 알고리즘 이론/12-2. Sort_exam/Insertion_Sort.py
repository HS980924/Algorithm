def Insert(N:int, arr:list):
    for i in range (1,N):
        for j in range(i):
            if(arr[i] <= arr[j]):
                tmp = arr[i]
                arr.remove(arr[i])
                arr.insert(j,tmp)
        print(i,arr)

if __name__ == "__main__":
    arr = [7,3,4,2,5,6,1]
    N = len(arr)
    Insert(N, arr)

    print(arr)