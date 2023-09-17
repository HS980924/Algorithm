# Upload BOJ Silver-4 Set 1764번 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr1 = set()
arr2 = set()

for _ in range(N):
    arr1.add(input().strip())
for _ in range(M):
    arr2.add(input().strip())

new_arr = list(arr1 & arr2)

new_arr.sort()
print(len(new_arr))
for person in new_arr:
    print(person)
