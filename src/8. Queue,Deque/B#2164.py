N = int(input())
start = 0
end = N-1
card = [i for i in range(1,N+1)]

for i in range(N-1):
    start += 1
    card.append(card[start])
    start += 1
    end += 1

print(card[start])