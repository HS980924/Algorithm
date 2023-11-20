# Upload BOJ Gold-5 math & Greedy 1041번 주사위
N = int(input())
dice = list(map(int,input().split()))

def twoSide():
    answer = max(dice)*2
    for i in range(6):
        tmp = dice[i]
        for j in range(6):
            if j != i and j != 5-i:
                if answer > tmp + dice[j]:
                    answer = tmp + dice[j]
    return answer

def threeSide():
    answer = max(dice)*3
    for i in [0,-1]:
        tmp = dice[i]
        for idxList in [[1,2],[2,4],[1,3],[3,4]]:
            if answer > tmp + dice[idxList[0]] + dice[idxList[1]]:
                    answer = tmp + dice[idxList[0]] + dice[idxList[1]]
    return answer

if N == 1:
    print(sum(dice)-max(dice))
else:
    min_oneSide = min(dice)
    min_twoSide = twoSide()
    min_threeSide = threeSide()
    total = 0

    total += min_oneSide*((N-2)*(N-2)*5 + (N-2)*4)
    total += min_twoSide*4*((N-2) + (N-1))
    total += min_threeSide*4

    print(total)
# ===================== 더 쉬운 풀이 =====================
sum=0  
sumLists=[]
if N == 1:
    dice.sort()
    for i in range(0,5):
        sum+=dice[i]
else:
    sumLists.append(min(dice[0],dice[5]))
    sumLists.append(min(dice[1],dice[4]))
    sumLists.append(min(dice[2],dice[3]))
    sumLists = sorted(sumLists)

    #1,2,3면이 보여질때 주사위 최소값
    min1 = sumLists[0]
    min2 = sumLists[0] + sumLists[1]
    min3 = sumLists[0] + sumLists[1] + sumLists[2]

    #1,2,3면이 보여지는 주사위 개수
    n1 = (N-2)*(N-2)*5 + (N-2)*4
    n2 = 4*((N-2) + (N-1))
    n3 = 4

    sum += n1 * min1
    sum += n2 * min2
    sum += n3 * min3

print(sum)