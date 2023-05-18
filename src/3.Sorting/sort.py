# ===================================================
#                       최형순
# ===================================================
# def Selection_Sort(N:int, Num:list):
#     for i in range(N):
#         ind = Num.index(min(Num[i:]))
#         tmp = Num[i] 
#         Num[i] = Num[ind]
#         Num[ind] = tmp
        # print(i, Num)

# def Insert(N:int, arr:list):
#     for i in range (1,N):
#         for j in range(i):
#             if(arr[i] <= arr[j]):
#                 tmp = arr[i]
#                 arr.remove(arr[i])
#                 arr.insert(j,tmp)
#         print(i,arr)

# N = int(input())
# Num = [int(input()) for i in range (N)]
# print(Num)
# Selection_Sort(N, Num)
# Insert(N, Num)

# print(Num)

# ===================================================
#                       이승현
# ===================================================
# arr=list(map(int, input().split()))
# print(arr)
# for i in range(len(arr)):
#     tmp = min(arr[i:])
#     arr.remove(tmp)
#     arr.insert(i,tmp)
#     print(i+1,arr)
# print(arr)
# ===================================================
#                       이규호
# ===================================================
# array = [7, 3, 4, 2, 5, 6, 1]
# cnt = 0
# print(array)
# while cnt < len(array):
#     a = array.index(min(array[cnt:]))
#     b = array.pop(cnt)
#     array.insert(a, b)
#     a = array.pop(a-1)
#     array.insert(cnt, a)
#     cnt += 1
#     print(array)

# print(array)

# ===================================================
#                       조민준
# ===================================================
# arr = [7,3,4,2,5,6,1]
# #print(arr)
# for i in range(len(arr)):
#     tmp = arr.index(min(arr[i:]))
#     arr[i], arr[tmp] = arr[tmp], arr[i] # SWAP
#     #print(i, arr)
# print(arr)


# arr = [7,3,4,2,5,6,1]
# print(arr)
# for i in range(len(arr)):
#     for j in range(i,-1,-1):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#             i = j
#     print(i,arr)

array = []
for i in range(int(input())):
    array.append(int(input()))

for i in range(len(array)):
    array[i], array[array.index(min(array[i:]))] = array[array.index(min(array[i:]))], array[i]
    print(i, array)

print(array)