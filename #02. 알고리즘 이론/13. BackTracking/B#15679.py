N, M = map(int, input().split())

stack = []
def sequenced():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return

    for i in range(1, N+1):
        if i in stack:
            continue
        stack.append(i)
        sequenced()
        stack.pop()
    
sequenced()