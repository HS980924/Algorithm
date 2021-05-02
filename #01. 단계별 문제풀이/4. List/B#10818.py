num = int(input())
arr = list(map(int,input().split()))
print(min(arr),max(arr)) # sum()


'''
min = 0
max = 0
for i in range (len(arr)):
    if(arr[min] > arr[i]):
        min = i
    if(arr[max] < arr[i]):
        max = i

print(arr[min],arr[max])
'''