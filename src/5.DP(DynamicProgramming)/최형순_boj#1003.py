if __name__ == "__main__":
    T = int(input())
    
    for i in range(T):
        N = int(input())
        tmp = []
        for i in range (N+1):
            if(i == 0):
                tmp.append([1,0])
            elif(i == 1):
                tmp.append([0,1])
            else:  
                tmp.append([int(tmp[i-1][0]) + int(tmp[i-2][0]),int(tmp[i-1][1]) + int(tmp[i-2][1])])
        print(' '.join(map(str,tmp[N])))
        
'''
zero = [1,0]
one = [0,1]
for i in range(2,40):
    zero.append("")
    one.append("")

def c(num):
    for i in range(2,num+1):
        if zero[i] == "" and one[i] == "":
            zero[i] = zero[i-2] + zero[i-1]
            one[i] = one[i-2] + one[i-1]
    return print("%d %d"%(zero[num],one[num]))


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        n = int(input())
        if n == 0:
            print(zero[0], one[0])
        elif n == 1:
            print(zero[1], one[1])
        else:
            c(n)
'''

'''
def fibonacci(n):
    t0 = [1, 0]
    t1 = [0, 1]
    if n >= 2:
        for p in range(2, n+1):
                t0.append(t0[p-1] + t0[p-2])
                t1.append(t1[p-1] + t1[p-2])

    print(t0[n], t1[n])

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        fibonacci(N)
'''