# 0 <= N <= 99 
# 주어진 수가 10 작다면 앞에 0을 붙여 두자리 수로 만들고 각 자리의 숫자를 더한다.
# 그 다음 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.

Lengh = 0
NewNum = 0
T = True

Num = int(input())
NewNum = Num

while T:
    if(NewNum == Num and Lengh != 0):
        T = False
    if NewNum < 10:
        NewNum = NewNum*2
    else:
        one_num = (NewNum // 10) + (NewNum % 10)
        Ten_num = NewNum %10
        NewNum = Ten_num*10 + one_num % 10
        Lengh += 1
    
    
print(Lengh+1)




