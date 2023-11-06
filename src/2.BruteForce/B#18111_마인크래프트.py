# Upload BOJ Silver-2 BruteForce 18111번 마인크래프트
import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())
blocks = [list(map(int,input().split())) for _ in range(N)]

min_time = int(1e9)
max_height = 0

for height in range(257):
    useBlock = 0
    getBlock = 0
    
    for i in range(N):
        for j in range(M):
            if blocks[i][j] < height:
                useBlock += height-blocks[i][j]
            else:
                getBlock += blocks[i][j]-height
    
    if getBlock + B >= useBlock:
        time = 2*getBlock + useBlock
        if time <= min_time:
            min_time = time
            max_height = height

print(min_time, max_height)