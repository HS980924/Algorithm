
def check(x, y, a):
    x_check = x // 3
    y_check = y // 3
    for i in range(9):
        if i // 3 == x_check:
            for j in range(9):
                if j // 3 == y_check:
                    if sudoku[i][j] == a:
                        return 1
    return 0


def Sudoku(cnt, x_zero, y_zero):
    global sudoku
    candidate = list(range(1, 10))

    if cnt == len(x_zero):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=" ")
            print(end="\n")
        return
    for i in range(len(x_zero)):
        if sudoku[x_zero[i]][y_zero[i]] == 0:
            for j in range(9):
                if sudoku[x_zero[i]][j] in candidate:
                    candidate.remove(sudoku[x_zero[i]][j])
                    candidate.remove(sudoku[j][x_zero[i]])
            if candidate:
                for k in candidate:
                    if check(x_zero[i], y_zero[i], k) == 0:
                        sudoku[x_zero[i]][y_zero[i]] = k
                        Sudoku(cnt+1, x_zero, y_zero)
                        sudoku[x_zero[i]][y_zero[i]] = 0


sudoku = []
x_zero = []
y_zero = []

for i in range(9):
    sudoku.append(list(map(int, input().split())))
print(x_zero)
Sudoku(0, x_zero, y_zero)