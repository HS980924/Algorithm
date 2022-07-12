def solution(N, number):
    dp = [[]]
    
    for i in range(1,9):
        tmp = []
        for j in range(1,i):
            for k in dp[j]:
                for x in dp[i-j]:
                    tmp.append(k+x)
                    if k-x > 0:
                        tmp.append(k-x)
                    tmp.append(k*x)
                    if x != 0 and k != 0:
                        tmp.append(k//x)
                        
        tmp.append(int(str(N)*i))
        if number in tmp:
            return i
        dp.append(list(set(tmp)))
        
    return -1



N = 5
num = 31168
print(solution(N,num))