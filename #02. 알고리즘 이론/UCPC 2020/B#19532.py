a,b,c,d,e,f = map(int,input().split())

for i in range(-999,1000):
    for j in range(-999,1000):
        if(a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)
'''
a,b,c,d,e,f = map(int,input().split())

y = int((c*d - f*a) / (b*d - e*a))
x = int((c*e - b*f) / (a*e - b*d))

print(x,y)
'''