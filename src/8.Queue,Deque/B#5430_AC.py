# Upload BOJ Gold-5 Deque 5430번 AC
from collections import deque

T = int(input())

for i in range(T):
    R_cnt = 0
    expression = list(input())
    N = int(input())
    arr = input()[1:-1].split(',')
    deq = deque(arr)
    error = False
    
    if N == 0:
        deq = []
    
    for exp in expression:
        if exp == 'R':
            R_cnt += 1
        else:
            if deq:
                if R_cnt % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()
            else:
                error = True
                break
    if error:
        print('error')
    else:
        if R_cnt % 2 == 0:
            print('['+','.join(deq)+']')
        else:
            deq.reverse()
            print('['+','.join(deq)+']')

