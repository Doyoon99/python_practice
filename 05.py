# 복잡한 계산기 만들기

import os
operator = ["+", "-", "*", "/", "="] # 연산자를 구별하기 위해 만든 리스트

def string_calculator(user_input, show_history=False):
    string_list = []
    lop = 0 # 마지막 연산자의 위치를 기억할 변수

    if user_input[-1] not in operator:
        user_input += "="

    # 숫자와 연산자를 리스트에 담는 for문
    for i, s in enumerate(user_input):
        if s in operator:
            if user_input[lop:i].strip() != "":
                string_list.append(user_input[lop:i])
                string_list.append(s)
                lop = i + 1

    string_list = string_list[:-1]

    pos = 0 # 현재 위치를 계산하는 변수
    while True:
        if pos + 1 > len(string_list):
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator:
            temp = string_list[pos-1] + string_list[pos] + string_list[pos + 1] # 숫자 + 연산자 + 숫자 따로 빼기
            del string_list[0:3]
            string_list.insert(0, str(eval(temp)))
            pos = 0

            if show_history: # 과정을 보여줌
                print(string_list)
        pos += 1
    if len(string_list) > 0:
        result = float(string_list[0])
    
    return round(result, 4)

while True:
    os.system("cls")
    user_input = input("계산식을 입력하세요 >> ")
    if user_input == "\exit":
        break
    result  = string_calculator(user_input, show_history = True)
    print("결과 : {}".format(result))
    os.system("pause")