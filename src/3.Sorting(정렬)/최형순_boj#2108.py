from collections import Counter
import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    Num = [int(sys.stdin.readline()) for i in range (N)]
    
    # 정렬
    Num.sort()

    avg = round(sum(Num) / N)
    print(avg)

    mid = Num[int((N-1)/2)]
    print(mid)

    cnt = Counter(Num).most_common()
    if len(Num) > 1: 
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0]) 
        else : 
            print(cnt[0][0]) 
    else : print(Num[0]) 
            
    ran = max(Num) - min(Num)
    print(ran)