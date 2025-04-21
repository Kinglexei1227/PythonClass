# 입력받은수의 구구단 출력기

# 사용자로부터 하나의 정수를 입력받는 입력란
num = int(input("출력할 단을 입력하세요 (2~9): "))

# 구구단 (짝수)
if 2 <= num <= 9 :
    for roh in range(2, 10, 2) :
        if num % 2 == 0:
            print(f"{num} X {roh} = {num * roh}")
# 예외처리
else:
    ("오류: 2단부터 9단까지만 입력 가능합니다.")
