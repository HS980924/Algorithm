#import sys
#input = sys.stdin.readline
queue = []
tmp_queue = []
def BFS(building, L, R, C):
    time = 0
    
    
    return time
    


while True:
    time = 0
    L, R, C = map(int, input().split())
    if L + R + C == 0:
        break
    else:
        building = []
        queue = []
        for i in range(L):
            tmp1 = []
            for j in range(R):    
                tmp2 = list(input())
                if "S" in tmp2:
                    queue.append([i,j,tmp2.index('S')])
                tmp1.append(tmp2)
            input()
            building.append(tmp1)
        
        BFS()
        
        
        
    
