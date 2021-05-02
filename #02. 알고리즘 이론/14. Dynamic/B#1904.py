if __name__ == "__main__":
    N = int(input())
    tail = [0]*N

    for i in range(N):
        if(i < 2):
            tail[i] = i+1
        else:
            tail[i] = (tail[i-1] + tail[i-2])%15746

    print(tail[N-1])
    
    