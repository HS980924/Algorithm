def solution(food):
    answer = ''
    for idx in range(1,len(food)):
        food_cnt = food[idx] // 2
        if food_cnt:
            answer += str(idx)*food_cnt
    reversed_answer = "".join(reversed(answer))
    answer += "0" + reversed_answer
    return answer