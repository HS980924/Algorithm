# Upload BOJ Silver-4 BS 2776번 암기왕
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    num1 = set(map(int,input().split()))
    
    M = int(input())
    num2 = list(map(int,input().split()))
    
    for value in num2:
        if value in num1:
            print(1)
        else:
            print(0)
        
    
    # num1.sort()
    # for value in num2:
    #     start = 0
    #     end = len(num1)-1
    #     answer = 0
        
    #     while start <= end:
    #         mid = (start + end) // 2
            
    #         if num1[mid] == value:
    #             answer = 1
    #             break
    #         elif num1[mid] < value:
    #             start = mid + 1
    #         else:
    #             end = mid - 1
            
    #     print(answer)