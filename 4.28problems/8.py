# 숫자 맞추기 게임 프로그램

# while문과 break문을 활용해 1부터 100사이의 숫자를 맞추는 게임

# 랜덤 함수
import random
ran = random.randint(1,100) # 1 부터 100까지 숫자 설정
ans = 0

# 맞출때 까지 반복
while ans != ran:
    ans = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
    # 정답, 오답 설정
    if ans == ran:
        print("정답입니다!")
        break
    elif ans > ran:
        print("더 작은 숫자입니다.")
    elif ans < ran:
        print("더 큰 숫자입니다.")
