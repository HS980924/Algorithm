N, M = map(int,input().split())
Card = list(map(int,input().split()))

Max = 0
for i in range(len(Card)-2):
    for j in range(i+1,len(Card)-1):
        for k in range(j+1,len(Card)):
            Current_s = Card[i] + Card[j] + Card[k]
            if(Current_s >= Max and Current_s <= M):
                Max = Current_s

print(Max)
'''
def Card_S(Card:list):
    Max = 0
    for i in range(len(Card)-2):
        for j in range(i+1,len(Card)-1):
            for k in range(j+1,len(Card)):
                Current_s = Card[i] + Card[j] + Card[k]
                if(Current_s >= Max and Current_s <= M):
                    Max = Current_s
    return Max

if __name__ == "__main__":
    N, M = map(int,input().split())
    Card = list(map(int,input().split()))
    print(Card_S(Card))
'''    