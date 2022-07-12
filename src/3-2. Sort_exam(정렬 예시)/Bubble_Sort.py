def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def Bubble(N:int, arr:list):
    for i in range(N-1,-1,-1):
        for j in range(i):
            if(arr[j] > arr[j+1]):
                swap(arr,j,j+1)
        print(arr)

if __name__ == "__main__":
    arr = [7,3,4,2,5,6,1]
    N = len(arr)
    Bubble(N, arr)

    print(arr)