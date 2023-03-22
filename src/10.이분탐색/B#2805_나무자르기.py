N, M = map(int,input().split())
trees = list(map(int,input().split()))

answer = 0    
maxHeight = max(trees)
minHeight = 0
    
while minHeight <= maxHeight:
    length = 0
    midHeight = (maxHeight + minHeight) // 2
    
    for tree in trees:
        if tree > midHeight:
            length += tree - midHeight
    
    if M <= length:
        answer = midHeight
        minHeight = midHeight + 1
    else:
        maxHeight = midHeight - 1
    
print(answer)