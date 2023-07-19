# Upload BOJ Gold-5 Greedy 센서
N = int(input())
K = int(input())

sensor = list(map(int,input().split()))
sensor.sort()

if N <= K:
    print(0)
else:
    dist = []
    for i in range(1,N):
        dist.append(sensor[i]-sensor[i-1])

    dist.sort()
    for i in range(K-1):
        dist.pop()

    print(sum(dist))

