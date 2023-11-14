# Upload BOJ Silver-1 Dequeue 13335번 트럭
from collections import deque
N, W, L = map(int,input().split())
trucks = deque(list(map(int,input().split())))
bridge = deque()

time = 0
cnt = 0
currentWeigth = 0

while cnt < N:
    
    if bridge and bridge[0][1] >= W:
        popWeight = bridge.popleft()
        currentWeigth -= popWeight[0]
        cnt += 1
    
    if len(bridge) <= W:
        
        for i in range(len(bridge)):
            bridge[i][1] += 1
            
        if trucks and currentWeigth + trucks[0] <= L:
            weight = trucks.popleft()
            bridge.append([weight,1])
            currentWeigth += weight
    time += 1
print(time)
        


