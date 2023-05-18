import sys
N = int(sys.stdin.readline())
start = 0
end = 0
queue = []

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "front":
        if start == end:
            print(-1)
        else:
            print(queue[start])
    elif command[0] == "back":
        if start == end:
            print(-1)
        else:
            print(queue[end-1])
    elif command[0] == "size":
        print(end-start)
    elif command[0] == "pop":
        if start == end:
            print(-1)
        else:
            print(queue[start])
            start += 1
    elif command[0] == "push":
        queue.append(command[1])
        end += 1
    elif command[0] == "empty":
        if start == end:
            print(1)
        else:
            print(0)