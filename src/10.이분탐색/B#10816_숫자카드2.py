# Upload BOJ Silver-4 BinarySearch 10816번 숫자카드2
import sys
input = sys.stdin.readline

N = int(input())
cards1 = list(map(int,input().split()))

M = int(input())
cards2 = list(map(int,input().split()))

sorted_card2 = sorted(cards2)
cardCntTable = dict()

def binarySearch(num):
    start = 0
    end = M-1
    
    while start <= end:
        mid = (start+end)//2
        
        if sorted_card2[mid] == num:
            return 1
        elif sorted_card2[mid] < num:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for value in cards1:
    if value in cardCntTable:
        cardCntTable[value] += 1
    else:
        result = binarySearch(value)
        if result:
            cardCntTable[value] = 1

for value in cards2:
    if value in cardCntTable:
        print(cardCntTable[value],end=' ')
    else:
        print(0,end=' ')



