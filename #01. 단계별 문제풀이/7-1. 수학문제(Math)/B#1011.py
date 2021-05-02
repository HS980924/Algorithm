import math
N = int(input())

for i in range (N):
    x, y = map(int,input().split())
    s = y - x
    a = math.trunc(math.sqrt(s))
    count = a
    sum = a

    while(sum < s):
        if(s-sum < a):
            a -= 1
        sum += a
        count += 1

    print(count)

'''
from sys import stdin

t = int(stdin.readline())

for i in range(t):
    d1, d2 = list(map(int, stdin.readline().split()))
    d = d2 - d1
    #d = int(input())
    
    n = int(d**0.5)

    if n == 1:
        print(d)
    elif d == n**2:
        print(2*n-1)
    elif d >= n*(n+1)+1:
        print(2*n+1)
    elif d >= n**2+1:
        print(2*n)
'''

'''
import math


def max_num(l):
    x = math.ceil(math.sqrt(l))
    if l <= x*(x-1):
        return 2*x-2
    else:
        return 2*x-1


def main():
    n = int(input())
    ans_list = []
    for i in range(n):
        a, b = map(int, input().split())
        ans_list.append(max_num(b-a))
    for i in ans_list:
        print(i)

if __name__ == '__main__':
    main()
'''