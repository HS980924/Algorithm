N = int(input())

for i in range(N):
    n,m = map(int,input().split())
    imp = list(map(int,input().split()))
    pos = [False]*n
    pos[m] = True
    cnt = 1
    
    while True:
        if imp[0] == max(imp):
            if pos[0]:
                print(cnt)
                break
            else:
                imp.pop(0)
                pos.pop(0)
                cnt += 1
        else:
            imp.append(imp.pop(0))
            pos.append(pos.pop(0))