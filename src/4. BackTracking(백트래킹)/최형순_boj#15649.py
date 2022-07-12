N, M = map(int, input().split())
tmp = [False]*N
tmp2 = []

def NM(N, M, cnt):
    if (M == cnt):
        print(' '.join(map(str, tmp2)))
        return

    for i in range(len(tmp)):
        if not tmp[i]:
            tmp[i] = True
            tmp2.append(i+1)
            NM(N, M, cnt+1)
            tmp[i] = False
            tmp2.pop()
NM(N,M,0)

'''
n, m = map(int, input().split())
a = [False] * n
b = [0] * m
def nm(result, n, m):
    if result == m:
        for i in range(m):
            print(b[i], end = ' ')
        print()
        return
    for j in range(n):
        if a[j]:
            continue
        a[j] = True
        b[result] = j+1
        nm(result+1, n, m)
        a[j] = False

nm(0, n, m)
'''