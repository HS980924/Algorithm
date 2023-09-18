# Upload BOJ silver-5 math 2563번 색종이
arr = [[0 for _ in range(101)] for _ in range(101)]

N = int(input())

for _ in range(N):
    start_x, start_y = map(int,input().split())
    
    for x in range(start_x, start_x+10):
        for y in range(start_y, start_y+10):
            arr[x][y] = 1
            
answer = 0
for x in arr:
    answer += sum(x)
print(answer)