# Upload BOJ Gold-5 Dequeue 13549번 숨바꼭질3
from collections import deque

N, K = map(int,input().split())

time = [0]*(100001)
queue = deque()
queue.append(N)
time[N] = 1

while queue:
    x = queue.popleft()

    if x == K:
        print(time[K]-1)
        break

    tmp = [x-1, x+1, x*2]

    for value in tmp:
        if 0 <= value < 100001 and not time[value]:
            if value == 2*x:
                time[value] = time[x]
                queue.appendleft(value)
            else:
                time[value] = time[x] + 1
                queue.append(value)
