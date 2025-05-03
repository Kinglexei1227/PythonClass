# 숫자 맞추기 확장 게임 프로그램

# while문과 break문을 활용해 1부터 100사이의 숫자를 맞추는 게임

# 랜덤 함수
import random
answer = random.randint(1,100)
# 최대 기회
total_attempt = 10
# 최대 10번 반복
for attempt in range(1, total_attempt + 1):
    print(f"기회 {attempt}/{total_attempt} - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력): ", end="")