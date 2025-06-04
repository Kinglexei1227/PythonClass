import random

# 사용자로부터 가위, 바위, 보 중 한가지 선택받기
luck = input("가위, 바위, 보 중 하나를 선택하세요: ")

# 난수를 생성하여 리스트에서 요소를 선택하는 방법
choices = ['가위', '바위', '보']
computer_choice = random.choice(choices)

if luck == choices:
    print("무승부 입니다!")