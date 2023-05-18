import sys

def Push(x):
    stack.append(x)

def Pop():
    if Empty() == 1:
        result = -1
    else:
        result = stack.pop()
    return result

def Empty():
    if len(stack)==0:
        return 1
    else:
        return 0

def Top():
    if Empty() == 1:
        return -1
    else:
        return stack[-1]


if __name__ == "__main__":
    N = int(input())
    stack = []

    for i in range(N):
        command = sys.stdin.readline().split()

        if(command[0] == 'push'):
            Push(command[1])
        elif(command[0] == 'pop'):
            print(Pop())
        elif(command[0] == 'size'):
            print(len(stack))
        elif(command[0] == 'empty'):
            print(Empty())
        elif(command[0] == 'top'):
            print(Top())
