def sort(arr,low, high):
    if high - low < 2:
        return
    mid = (low + high) // 2
    sort(arr, low, mid)
    sort(arr, mid, high)
    merge(low, mid, high)

def merge(low, mid, high):
    temp = []
    l, h = low, mid

    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[h])
            h += 1

    while l < mid:
        temp.append(arr[l])
        l += 1
    while h < high:
        temp.append(arr[h])
        h += 1

    for i in range(low, high):
        arr[i] = temp[i - low]

if __name__ == "__main__":
    arr = [7,3,4,2,5,6,1]
    sort(arr,0,len(arr))
    print(arr)