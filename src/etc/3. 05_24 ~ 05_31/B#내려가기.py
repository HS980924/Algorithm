#maxDp = [[0 for _ in range(3)] for _ in range(N+1)]  메모리 초과
#minDp = [[0 for _ in range(3)] for _ in range(N+1)]  메모리 초과
import sys

def solution():
    input = sys.stdin.readline
    result = [0,0]
    maxDp = [[0 for _ in range(3)] for _ in range(2)]
    minDp = [[0 for _ in range(3)] for _ in range(2)]
    N = int(input())
    
    for i in range(N):
        board = list(map(int,input().split()))
        for j in range(3):
            if j == 0:
                maxDp[1][j] = max(maxDp[0][j], maxDp[0][j+1]) + board[j]
                minDp[1][j] = min(minDp[0][j], minDp[0][j+1]) + board[j]
            elif j == 1:
                maxDp[1][j] = max(maxDp[0][j-1], maxDp[0][j], maxDp[0][j+1]) + board[j]
                minDp[1][j] = min(minDp[0][j-1], minDp[0][j], minDp[0][j+1]) + board[j]
            else:
                maxDp[1][j] = max(maxDp[0][j-1], maxDp[0][j]) + board[j]
                minDp[1][j] = min(minDp[0][j-1], minDp[0][j]) + board[j]
                
        for j in range(3):
            maxDp[0][j] = maxDp[1][j]
            minDp[0][j] = minDp[1][j]
            
    result[0] = max(maxDp[1])
    result[1] = min(minDp[1])
    return result


print(*solution())
