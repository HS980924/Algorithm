# 설탕 배달 nKg
# 설탕은 봉지에 담김
# 봉지는 3Kg or 5Kg
# 최대한 적은 봉지를 들고 감
# 3 혹은 5에 꽉 안차면 -1 출력

# N = 5x + 3y   (x+y)
# N != 5x + 3y  (-1)
def sugar(N: int):
    size_f = N//5
    size_th = N//3
    for i in range (0,size_th+1):
        for j in range (0,size_f+1):
            if(3*i + 5*j == N):
                return i+j
            elif(3*i + 5*j > N):
                break
    return -1


if __name__ == "__main__":
    N = int(input())
    ans = sugar(N)
    print(ans)


