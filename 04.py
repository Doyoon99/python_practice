# 간단한 계산기 만들기

import os

while True:
    os.system("cls")
    s = input("계산식 입력> ")
    print("결과: {}".format(eval(s)))
    os.system("pause")
