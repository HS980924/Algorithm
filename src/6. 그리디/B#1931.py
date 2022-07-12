N = int(input())
office = []

for i in range(N):
    S, E = map(int,input().split())
    office.append([S,E])

office.sort(key=lambda x : (x[1], x[0]))

cnt = 1 
end_time = office[0][1]
for i in range(1, N):
    if office[i][0] >= end_time: 
        cnt += 1 
        end_time = office[i][1] 

print(cnt)