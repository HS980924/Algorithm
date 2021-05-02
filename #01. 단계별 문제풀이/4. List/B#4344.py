Test_case = int(input())

for i in range (Test_case):
    score = list(map(int,input().split()))
    Avg = sum(score[1:]) / score[0]

    count = 0
    for i in range (1, len(score)):
        if(Avg < score[i]):
            count += 1
    rate = (count / score[0]) * 100

    print(format(rate, ".3f")+'%')
    # print(f'{rate:.3f}%')
    # print("%0.3f" % average[i])