X = []
Y = []
for i in range (3):
    x, y = map(int,input().split())
    X.append(x)
    Y.append(y)

for i in range (3):
    if(X.count(X[i]) == 1):
        print(X[i], end = " ")
        break

for i in range (3):
    if(Y.count(Y[i]) == 1):
        print(Y[i])
        break
        