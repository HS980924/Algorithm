from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    command = list(map(str,input().split()))
    
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    else:
        if queue:
            print(0)
        else:
            print(1)

