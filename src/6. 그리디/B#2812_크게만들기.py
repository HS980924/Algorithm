N, K = map(int, input().split())
number = list(input())
stack = []

for num in number:
    while stack and stack[-1] < num and K:
        stack.pop()
        K -= 1
    stack.append(num)


print(''.join(stack[:len(stack)-K]))
