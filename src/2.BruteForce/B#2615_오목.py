# Upload BOJ silver-1 Brute-force 2615번 오목
# 참고 블로그 : https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2615-%EC%98%A4%EB%AA%A9-Brute-Force
import sys
board = [list(map(int,input().split())) for _ in range(19)]
visited = [[0 for _ in range(19)] for _ in range(19)]
win = 0
ways = [[0,1],[1,0],[1,1],[-1,1]]
answer = []


for x in range(19):
    for y in range(19):
        if board[x][y]:
            target = board[x][y]
            
            for i in range(4):
                cnt = 1
                nx = x + ways[i][0]
                ny = y + ways[i][1]
                
                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == target:
                    cnt += 1
                    
                    if cnt == 5:
                        # 육목 체크
                        if 0 <= x-ways[i][0] < 19 and 0 <= y-ways[i][1] < 19 and board[x-ways[i][0]][y-ways[i][1]] == target:
                            break
                        if 0 <= nx + ways[i][0] < 19 and 0 <= ny+ways[i][1] < 19 and board[nx+ways[i][0]][ny+ways[i][1]] == target:
                            break
                        print(target)
                        print(x+1,y+1)
                        sys.exit(0)
                    
                    nx += ways[i][0]
                    ny += ways[i][1]

print(0)