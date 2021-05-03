#숫자 야구 게임

import random
import os

numbers = []
number = str(random.randint(0,9))

for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9)) #번호 재생성
    numbers.append(number)

os.system("cls")

print("*" * 60)
print("야구게임을 시작합니다!!!")
print("*" * 60)

count_strike = 0
count_ball = 0

while count_strike < 3:

    count_strike = 0
    count_ball = 0

    # '1', '2', '3' 이런 식으로 인덱싱하기 위해서 문자열로 숫자 받음
    num = str(input("숫자 3자리를 입력하세요 >> "))
    if len(num) == 3:
        for i in range(0, 3):
            for j in range(0,3):
                if num[i] == numbers[j] and i == j:
                    count_strike += 1
                elif num[i] == numbers[j] and i != j:
                    count_ball += 1
        if count_strike == 0 and count_ball == 0:
            print("3 아웃!!")
        else:
            output = ""
            if count_strike > 0:
                output += "{} 스트라이크".format(count_strike)
            if count_ball > 0:
                output += "{} 볼".format(count_ball)

            print (output.strip())

print("게임성공")

                
