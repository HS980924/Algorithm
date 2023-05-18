if __name__ == "__main__":
    N = int(input())
    arr = []

    for i in range(N):
        x, y = map(int,input().split())
        arr.append([x,y])

    sorted_arr = sorted(arr)

    for x,y in sorted_arr:
        print(x,y)


