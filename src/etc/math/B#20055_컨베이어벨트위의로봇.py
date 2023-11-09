# Upload BOJ Gold-5 20055번 컨베이어 벨트 위의 로봇 implement
from collections import deque 

N, K = map(int,input().split())
belt = deque(list(map(int,input().split())))
isRobot = deque([0]*N)
answer = 0
    
def robot_Rotation():
    for i in range(N-2,-1,-1):
        if isRobot[i]:
            if not isRobot[i+1] and belt[i+1]:
                belt[i+1] -= 1
                isRobot[i+1] = 1
                isRobot[i] = 0

def put_robot():
    if belt[0]:
        isRobot[0] = 1
        belt[0] -= 1
        
while True:
    answer += 1
    
    belt.rotate(1)
    isRobot.rotate(1)
    
    isRobot[-1] = 0
    
    robot_Rotation()
    
    isRobot[-1] = 0
    
    put_robot()
    
    if belt.count(0) >= K:
        break
    
print(answer)



# N = 3, K = 2
# 1 2 1 2 1 2
    # 1-1단계(벨트 회전)
    # 2 1 2 1 2 1
    # 0 0 0 
    
    # 1-2단계(로봇 회전)
    # 2 1 2 1 2 1
    # 0 0 0 
    
    # 1-3단계(로봇 올리기)
    # 1 1 2 1 2 1
    # 1 0 0
    
    # 2-1단계(벨트 회전)
    # 1 1 1 2 1 2
    # 0 1 0
    
    # 2-2단계(로봇 회전)
    # 1 1 0 2 1 2
    # 0 0 1
    
    # 2-3단계(로봇 올리기)
    # 0 1 0 2 1 2
    # 1 0 0
# -----------------------------------------------
    
    # 1-1단계(로봇 올리기)
    # 0 2 1 2 1 2
    # 1 0 0
    
    # 1-2단계(벨트 회전)
    # 2 0 2 1 2 1
    # 0 1 0
    
    # 1-3단계(로봇 회전)
    # 2 0 1 1 2 1
    # 0 0 1
    
    # 2-1단계(로봇 올리기)
    # 1 0 1 1 2 1
    # 1 0 0
    
    # 2-2단계(벨트 회전)
    # 1 1 0 1 1 2
    # 0 1 0
    
    # 2-3단계(로봇 회전)
    # 1 1 0 1 1 2
    # 0 1 0
    
    # 3
    