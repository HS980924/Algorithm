# 1. 도넛 그래프
# 정점 수 = 간선 수
# size 1 => 정점 수 : 1(n), 간선 수 : 1(n)
# size 2 => 정점 수 : 2(n), 간선 수 : 2(n)

# 2. 막대 그래프
# 정점 수 = 간선 수 + 1
# size 1 => 정점 수 : 2(n+1), 간선 수 : 1(n)
# size 2 => 정점 수 : 3(n+1), 간선 수 : 2(n)


# 3. 8자 그래프
# 정점 수 = 간선 수 + 1
# size 1 => 정점 수 : 3(2n+1), 간선 수 : 4 (2n+2)
# size 2 => 정점 수 : 5(2n+1), 간선 수 : 6 (2n+2)

from collections import defaultdict
def solution(edges):
    answer = [0] * 4
    endNum = 0

    nodeDirect = dict()

    for v1, v2 in edges:
        if not v1 in nodeDirect:
            nodeDirect[v1] = []
        nodeDirect[v1].append(v2)
        endNum = max(endNum, v1, v2)
    
    # 시작 정점 찾기
    existed = [0]*(endNum+1)
    for valueList in nodeDirect.values():
        print(valueList)
        for value in valueList:
            existed[value] = 1
    
    length = 0
    startInd = 0
    for idx, nodeNum in enumerate(existed):
        if idx == 0:
            continue
        if not nodeNum:
            if (length <= len(nodeDirect[idx])):
                startInd = idx
                length = len(nodeDirect[idx])

    answer[0] = startInd
    visited = [0]*(endNum+1)
    
    # 그래프 찾기
    for node in nodeDirect[startInd]:
        stack = []
        nodeCnt = 0
        edgeCnt = 0
        stack.append(node)

        while(stack):
            popNode = stack.pop()
            if visited[popNode]:
                continue
            visited[popNode] = 1
            nodeCnt += 1
            if popNode in nodeDirect:
                for nextNode in nodeDirect[popNode]:
                    stack.append(nextNode)
                    edgeCnt += 1
        if(edgeCnt == nodeCnt):
            answer[1] += 1
        elif(nodeCnt - 1 == edgeCnt):
            answer[2] += 1
        elif(nodeCnt + 1 == edgeCnt):
            answer[3] += 1

    return answer


def solution2(edges):
    answer = [0] * 4
    cntDict = {}

    for node1, node2 in edges:
        if not node1 in cntDict:
            cntDict[node1] = [0, 0]
        if not node2 in cntDict:
            cntDict[node2] = [0, 0]
        # [나가는 간선 수, 들어오는 간선 수]
        cntDict[node1][0] += 1
        cntDict[node2][1] += 1
    
    for key, edgeInfo in cntDict.items():
        if(edgeInfo[0] >= 2 and edgeInfo[1] == 0):
            answer[0] = key
        # 막대 그래프
        elif(edgeInfo[0] == 0 and edgeInfo[1] >= 1):
            # edgeInfo[1] >= 1 ( 생성된 정점에서 들어올 수 있기에, 그러면 들어오는 간선 수가 2가 됨 )
            answer[2] += 1
        # 8자 그래프
        elif(edgeInfo[0] == 2 and edgeInfo[1] >= 2):
            # edgeInfo[1] >= 2 ( 생성된 정점에서 들어올 수 있기에, 그러면 들어오는 간선 수가 3이 됨 )
            answer[3] += 1
    
    answer[1] = cntDict[answer[0]][0] - (answer[2] + answer[3])

    return answer


edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
edges2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 3], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
edges3 = [[1,1],[2,3],[3,2],[4,1],[4,2]]
print(solution2(edges))