# Upload BOG Silver-1 BFS 숨바꼭질 

from collections import deque

N, K = map(int, input().split())

maps = [0]*(100001)
q = deque();
q.append(N)
maps[N] = 1

while q:
    x = q.popleft()
    
    if x == K:
        print(maps[K]-1)
        break
    
    tmp = [x-1, x+1, x*2]
    
    for nx in tmp:
        if 0 <= nx < 100001:
            if not maps[nx]:
                maps[nx] = maps[x] + 1
                q.append(nx)
