# def solution(X, Y):
#     answer = ''
    
#     newSet = set(list(X)) & set(list(Y))
#     newList = list(newSet) 
#     newList.sort(reverse=True)
    
#     if(newList):
#         return ''.join(s for s in newList)
#     else:
#         return "-1"
    
    
def solution(X, Y):
    x_dic = {}
    y_dic = {}
    answer = ""
    for i in range(10):
        x_dic[i] = 0
        y_dic[i] = 0
    
    for value in X:
        x_dic[int(value)] += 1
    for value in Y:
        y_dic[int(value)] += 1
    
    
    for idx in range(9,-1,-1):
        cnt = min(x_dic[idx],y_dic[idx])
        answer += str(idx)*cnt
    
    if answer == "":
        answer += "-1"
    if answer[0] == "0":
        answer = "0"
    return answer

def solution(X, Y):
    answer = ""
    x_list = list(X)
    y_list = list(Y)
    
    x_list.sort()
    y_list.sort()
    
    # print(x_list)
    # print(y_list)
    
    while len(x_list) > 0 and len(y_list) > 0:
        if int(x_list[-1]) == int(y_list[-1]):
            answer += str(x_list.pop(-1))
            y_list.pop(-1)
        elif int(x_list[-1]) > int(y_list[-1]):
            x_list.pop(-1)
        else:
            y_list.pop(-1)
    
    if answer == "":
        answer = "-1"
   
    return str(int(answer))


X = "5525"
Y = "1255"	
print(solution(X,Y))