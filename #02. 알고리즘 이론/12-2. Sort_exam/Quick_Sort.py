def Swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def Quick(left:int, right:int):
    global arr
    pl = left
    pr = right
    pivot = arr[(pl+pr)//2]

    while(pl<=pr):
        while(arr[pl] < pivot):
            pl += 1
        while(arr[pr] > pivot):
            pr -= 1
        if(pl <= pr):
            Swap(arr,pl,pr)
            pl += 1
            pr -= 1

    if(left < pr):
        Quick(left, pr)
    if(pl < right):
        Quick(pl, right)
        
if __name__ == "__main__":
    arr = [7,3,4,2,5,6,1]
    N = len(arr)
    Quick(0,N-1)

    print(arr)

'''
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)
'''