N = int(input())
board = []

for i in range(N):
    board.append(list(map(int, input().split())))

print(board)