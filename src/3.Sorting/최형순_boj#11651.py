if __name__ == "__main__":
    N = int(input())
    arr = []

    for i in range(N):
        x, y = map(int,input().split())
        arr.append([y,x])

    sorted_arr = sorted(arr)

    for y,x in sorted_arr:
        print(x,y)


