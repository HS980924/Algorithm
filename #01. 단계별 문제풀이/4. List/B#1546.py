num = int(input())
arr = list(map(int, input().split()))
New_arr = [0]*num

for i in range (0,num):
    New_arr[i] = (arr[i] * 100 )/max(arr)

print(sum(New_arr)/num)