def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def Bubble_Sort(N:int, arr:list):
    for i in range(N):
        for j in range(N-1-i):
            if (arr[j] > arr[j+1]):
                swap(arr,j,j+1)

def Print_Arr(N:int, arr:list):
    for i in range(N):
        print(arr[i])

if __name__ == "__main__":
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    
    Bubble_Sort(N,arr)
    Print_Arr(N,arr)
    