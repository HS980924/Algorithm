def bsearch(ss, x):
    return bsearch_range( ss, x, range(len(ss)) )

# 아래 bsearch_range 함수를 작성하면 된다 (7점)
def bsearch_range(ss, x, r):
    if len(r) > 0:
        print("\n")
        print("range범위 = ",r)
        print("len(r) : ",len(r))
        mid = (r.start + r.stop-1) // 2
        print("mid :",mid)
        print("list[mid] = ",ss[mid])
        if x == ss[mid]:
            i,j = 0,0
            while ss[mid-i-1] == x:
                i += 1
            while ss[mid+j] == x:
                j += 1
            r = range(mid-i,mid+j)
            return r
        elif x < ss[mid]:
            print("x < ss[mid]")
            print("다음 range범위(r[:mid]) : ",r[:mid])
            print("다음 range범위(range(r.start,mid)) : ",range(r.start,mid))
            #return bsearch_range(ss, x, range(r.start,mid))
            return bsearch_range(ss, x, r[r.start:mid])
        else:
            print("x > ss[mid]")
            print("다음 range범위(r[mid+1:]) : ",r[mid+1:])
            print("다음 range범위(range(mid+1,r.stop)) : ",range(mid+1,r.stop))
            #return bsearch_range(ss, x, range(mid+1,r.stop))
            if (len(r[mid+1:]) == 0):
                return bsearch_range(ss, x, r[mid:])
            return bsearch_range(ss, x, r[mid+1:])
    else:
        print("return")
        return r


s3 = [1,4,2,6,8,2,3,6,9,10]
#s3 = [1,2,2,2,3,6]
s3.sort()
ss = [0,1,2,3,4,5,6,7,8,9]
print(ss)
print(s3)
print(bsearch(s3, 3)) # == range(4,5)  # 길이 1인 range 객체
print(bsearch(s3, 2)) # == range(1,4)  # 길이 3인 range 객체
#print(bsearch(s3, 5)) #  == range(5,5)  # 길이 0인 range 객체