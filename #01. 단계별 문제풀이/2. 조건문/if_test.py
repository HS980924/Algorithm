# if, else elif 조건문
"""
if -> if
else -> else
elif -> else if

조건문 끝에는 콜론(:)을 붙여 문법이 이어진다는 것을 알려야하며 파이썬은 들여쓰기가 상당히 중요하다.
ex) if 주머니 == 1000원: 
        복권 구매
    elif 주머니 == 500원:
        껌 구매
    else:
        Go to home
"""
# if, else문 사용
name = "BlockDMask"
if name == "BlockDMask":
    print("이름이 맞습니다.")
else:
    print("이름이 다릅니다.")

# if, elif, else문 사용
pocket = 1000
if pocket == 1000:
    print("Buy Lottery ticket")
elif pocket == 500:
    print("Buy Chewing gum")
else:
    print("Go to home")

"""
not -> 부정을 하는 역할
or -> c언어로 || (~ 이거나 ~이다.)역할
and -> c언어로 && (~ 이고 ~이다.)역할
"""

# 다양한 if 조건문 예제
a = "사과"
b = "바나나"
c = "치즈"

if a == "사과" or b == "안바나나":
    print("사과 이거나 바나나 입니다.")
if a == "사과" and b == "바나나":
    print("사과 이고 바나나 입니다.")
if not a == "사과":
    print("사과가 아니어야 여기로 들어옵니다.")
a = [1,2,3,4,5,6,7,8]
if 1 in a:
    print("a 리스트에 1이 포함")
elif 10 in a:
    print("a 리스트에 10이 포함 되어있습니디.")

#조건문에서 아무 일도 하지 않게 설정하기
pocket = ['paper', 'money','cellphone']
if 'money' in pocket:
    pass        #continue같은 느낌의 역할
else:
    print("카드를 꺼내라")

#if문을 한 줄로 작성
pocket = 1000
if pocket == 1000: print("Buy Lottery ticket")
elif pocket == 500: print("Buy Chewing gum")
else: print("Go to home")
