import sys
N = int(input())
Tree = [[] for _ in range(N+1)]

for i in range(N):
    arr = list(map(str,sys.stdin.readline().split()))
    root = ord(arr[0])-64
    left = ord(arr[1])-64
    right = ord(arr[2])-64
    Tree[root].append(left)
    Tree[root].append(right)

def Preorder_traversal(start):
    if start > 0:
        print(chr(start+64),end="")
        Preorder_traversal(Tree[start][0])
        Preorder_traversal(Tree[start][1])
       

def inorder_traversal(start):
    if start > 0:
        inorder_traversal(Tree[start][0])
        print(chr(start+64),end="")
        inorder_traversal(Tree[start][1])
        

def postorder_traversal(start):
    if start > 0:
        postorder_traversal(Tree[start][0])
        postorder_traversal(Tree[start][1])
        print(chr(start+64),end="")


Preorder_traversal(1)
print("")
inorder_traversal(1)
print("")
postorder_traversal(1)