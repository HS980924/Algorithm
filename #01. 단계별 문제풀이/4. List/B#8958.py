case = int(input())

for i in range (0,case):
    answer = input()
    count = 1
    score = 0
    for j in range (len(answer)):
        if(answer[j] == "O"):
            score = score + count
            count += 1
        else:
            count = 1
    print(score)
    
