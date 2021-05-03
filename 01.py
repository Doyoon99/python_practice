#숫자 맞히기 게임

import random
import os

#입력 받는 함수
def input_check(msg, casting=int):
    while True:
        try:
            user_input = casting(input("몇일까요?"))
            return user_input
        except:
            continue

chance = 10
count = 0

number = random.randint(1, 99) #1부터 99 중 숫자 1개 랜덤 선택
os.system("cls") #배쉬 창 깨끗하게 지우기
print("1부터 99까지의 숫자를 10번 안에 맞춰보세요.")

#숫자 게임 알고리즘
while count < chance: 
    count += 1
    user_input = input_check("몇 일까요?") #함수 사용
    if number == user_input:
        break
    elif user_input < number:
        print("{} 보다 큰 숫자입니다.".format(user_input))
    elif user_input > number:
        print("{} 보다 작은 숫자입니다.".format(user_input))

#결과
if user_input == number:
    print("성공! {} 맞습니다.".format(number))
else:
    print("실패, 정답은 {} 입니다.".format(number))