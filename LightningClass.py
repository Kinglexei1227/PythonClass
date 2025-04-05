# 변수
# 1) 지역변수
# 2) 전역변수

# 접근범위, 생명주기


# 정수 3개를 입력 받고

# 평균을 반환하는 함수 정의하시오.
def c():
    print("c 함수 호출")
    print("c 함수 종료")


def b():
    print("b 함수 호출")
    c()
    print("b 함수 종료")


def a():
    print("a 함수 호출")
    b()
    print("a 함수 종료")

a()