def solution(bridge_length, weight, truck_weights):
    time = 0
    stack = []
    
    while stack != [] or truck_weights != []:
        time += 1
        if truck_weights != []:
            if truck_weights[0] + sum(stack) <= weight and len(stack) < bridge_length:
                stack.append(truck_weights.pop(0))
                
        if time % bridge_length == 0:
            stack.pop(0)
    
    return time



b = 100
w = 100
t = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(b,w,t))

s = [1,1]
s += 1
print(s)