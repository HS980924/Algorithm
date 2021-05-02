#4:15
#5:50
S = input()
T = input()

S_length = len(S) 
T_length = len(T)
status = 0

if(S_length < T_length):
    Max_String = list(str(T))*2
    Min_String = list(str(S))
else : 
    Max_String = list(str(S))*2
    Min_String = list(str(T))

i = 0
while(i < len(Max_String)):
    for j in range (0,len(Min_String)):
        if(i < len(Max_String)):
            if (Max_String [i] == Min_String[j]):
                status = 1
                i += 1
            else : 
                status = 0
                break
    if(status == 0) :
        break


print(status)
