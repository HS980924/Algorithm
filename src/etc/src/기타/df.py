from collections import OrderedDict
def coins(n):
    clist = [0] # 0원일때는 0개만으로 초기화
    cnt = 0
    value = n

    for i in range(1,n+1):
    # coins[i-1] 까지는 채워져 있다 
    # i원을 지불할 때 사용할 수 있는 동전들 mycoins
        mycoins = [x for x in [7,5,2,1] if x <= i]
        clist.append( 1 + min([clist[i-x] for x in mycoins]) )

    print(mycoins)

    result = {x: 0 for x in mycoins}
    for coin in mycoins:
        if value // coin > 0:
            coin_cnt = value // coin
            value -= coin * coin_cnt
            result[coin] = coin_cnt
            print(result)
        else:
            result.pop(coin)

    print(result)
    d1 = dict(sorted(result.items(), reverse = True))
    return (clist[n], d1)

print(coins(12))