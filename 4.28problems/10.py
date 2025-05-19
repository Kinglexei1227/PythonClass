# 숫자 맞추기 확장 게임 프로그램

# while문과 break문을 활용해 1부터 100사이의 숫자를 맞추는 게임

# 랜덤 함수
import random

# 랜덤함수가 선택한 숫자 (1~100)
secret = random.randint(1, 100)
total_attempts = 10

print("=== 숫자 맞추기 게임 ===")

for attempt in range(1, total_attempts + 1):
    print(f"기회 {attempt}/{total_attempts} - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력): ", end="")
        
    guess = int(input())
        # 0 입력시 프로그램 종료
    if guess == 0:
        print("게임을 종료합니다.")
        break
        # 업다운
    if guess < secret:
        print("더 큰 숫자입니다.")
    elif guess > secret:
        print("더 작은 숫자입니다.")
    else: # 정답
        print("정답입니다!")
        print("게임이 끝났습니다.")
        break
else:
    print(f"모든 기회를 사용하였습니다. 정답은 {secret}입니다.")