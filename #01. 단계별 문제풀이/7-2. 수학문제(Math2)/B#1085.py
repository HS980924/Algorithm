x, y, w, h = map(int,input().split())
a = []
a.append(abs(w - x))
a.append(abs(y - h))
a.append(abs(x - 0))
a.append(abs(y - 0))

print(min(a))
