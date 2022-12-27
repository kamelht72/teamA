# -*- coding: utf-8 -*-
# main-1.py
import random
import tkinter

# 1dptj 100사의 임의 정수 생성
random_number = random.randint(1, 100)

#print(random_number)

# 게임 카운트 대입 또는 바인딩
game_count = 1

while True: # 맞추때까지 무한 반복
    try: # 에러가 발생하지 않을 때 동작
        # 사용자로부터 1과 100사이의 숫자 입력    
        my_number = int(input("1-100 사이의 숫자를 입력하세요:"))
        
        # 입력숫자가 랜덤변수보다 크면 '다운'이란 메시지를 알림
        if my_number > random_number:
            print("다운")
        # 입력숫자가 랜덤변수보다 작으면 '업'이란 메시지를 알림
        elif my_number < random_number:
            print("업")
        # 입력숫자가 랜덤변수와 같다면 축하합니다란 메시지와 맞추횟수를 출력
        elif my_number == random_number:
            print()
            print(f"축하합니다. {game_count}회 만에 맞췄습니다.")
            break
        
        game_count = game_count + 1
    except: # try 문 안에서 에러가 발생하면 except문 실행
        print("에러가 발생하였습습니다. 숫자를 입력하세요")
        