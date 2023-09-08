def solution(brown, yellow):
    answer = []
    divisor = []
    area = brown + yellow
    for i in range(1,int(area**0.5)+1):
        if area % i == 0:
            divisor.append(i)
    
    for value in divisor:
        col = value
        row = area // col
        brown_cnt = row *2 + (col-2)*2
        if brown_cnt == brown:
            answer.append(row)
            answer.append(col)
            break
    return answer


print(solution(10,2))