N, K = map(int,input().split())
yose = [i for i in range(1,N+1)]
result = []

while yose:
    for i in range(K-1):
        yose.append(yose.pop(0))
    result.append(yose.pop(0))
    print(yose)

result_str = str(result)[1:-1]
print("<"+result_str+">") 


