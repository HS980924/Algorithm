def change(n,k):
    result = []
    while n:
        result.append(n%k)
        n //= k
        
    return result[::-1]

def check_PrimeNum(n):
    if n == 1:
        return False
    elif n <= 3:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def foundPrime(value):
    Numlist = []
    cnt = 0
    tmp = ''
    for x in value:
        if x != 0:
            tmp += str(x)
        else:
            if tmp:
                Numlist.append(int(tmp))
            tmp = ''
    if tmp:
        Numlist.append(int(tmp))
        
    for x in Numlist:
        if check_PrimeNum(x):
            cnt += 1
    
    return cnt
        
def solution(n, k):
    answer = -1
    value = change(n,k)
    answer = foundPrime(value)
    
    return answer

print(solution(1,3))