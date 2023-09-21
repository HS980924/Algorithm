# Upload BOJ Silver-4 Hash 17219번 비밀번호 찾기
N, M = map(int,input().split())
hash = dict()

for _ in range(N):
    key, value = map(str, input().split())
    hash[key] = value

for _ in range(M):
    key = input()
    print(hash[key])
