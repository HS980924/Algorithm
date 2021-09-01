while True:
    stack = []
    sentence = input()

    if sentence == ".":
        break

    else:
        for x in sentence:
            if x == '[' or x == '(':
                stack.append(x)
            elif x == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(x)
                    break
            elif x == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(x)
                    break
            else:
                continue

        if stack:
            print("no")
        else:
            print('yes')