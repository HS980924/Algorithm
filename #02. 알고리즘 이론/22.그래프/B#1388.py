n, m = map(int, input().split())
li = [input() for _ in range(n)]
cnt = 0
for i in range(n):
    j = 0
    while j < m:
        if li[i][j] == '|':
            j += 1
        else:
            cnt += 1
            while j < m and li[i][j] == '-':
                j += 1
for j in range(m):
    i = 0
    while i < n:
        if li[i][j] == '-':
            i += 1
        else:
            cnt += 1
            while i < n and li[i][j] == '|':
                i += 1
print(cnt)