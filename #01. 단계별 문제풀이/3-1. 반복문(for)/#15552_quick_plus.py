# input 대신 sys.stdin.readline을 사용 import sys 사용
# Python function
# 1. Built-in function (= 내장 함수) -> input()
# 2. Thrid-party module (= 외부 라이브러리) -> sys.stdin.readline
import sys

N = int(input())

for i in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1+num2)