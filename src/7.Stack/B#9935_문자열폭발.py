# Upload BOJ Gold-4 Stack 문자열폭발
s = input()
pattern = list(input())
stack = []

for i in range(len(s)):
    stack.append(s[i])
    if len(stack) >= len(pattern):
        if stack[len(stack)-len(pattern):] == pattern:
            for cnt in range(len(pattern)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")

