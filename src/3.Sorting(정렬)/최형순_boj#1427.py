if __name__ == "__main__":
    N = input()
    arr = list(map(int,N))

    arr.sort(reverse = True)

    for i in range(len(arr)):
        print(arr[i],end="")