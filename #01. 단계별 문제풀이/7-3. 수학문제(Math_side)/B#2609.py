Num1, Num2 = map(int,input().split())
# 최대공약수
# 최소공배수
i = 2
Num1_arr = []
Num2_arr = []
while(Num1 > 0 or Num2 > 0):
    if(Num1 / i == 0):
        Num1_arr.append(i)    
    if(Num2 / i == 0):
        Num2_arr.append(i)