index = 0;
# arr = [0]*9
arr = [int(input()) for _ in range (9)]

#for i in range (0,9):
#    arr[i] = int(input())

'''
for i in range (1,9):
    if(arr[index] < arr[i]):
        index = i
'''

# print(max(arr),index+1)

print(max(arr),arr.index(max(arr))+1)

# 리스트 이름.index(max(리스트 이름))
# 리스트 최대 값의 인덱스를 찾는 함수

