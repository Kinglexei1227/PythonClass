
# 변수의 scope 관점
# 1) Global variable (전역변수)
#   -> 함수 밖에서 선언된 변수
#   -> B: 변수 선언
#   -> D: 프로그램 종료 시
#
# 2) Local variable (지역변수)
#   -> 함수 내 선언된 변수

def getName(arg_name):
    name = arg_name + "님"
    return name

def getGreeting(arg_name):
    greeting = arg_name + "안녕하세요"
    return greeting

def prtShow(arg_name):
    name = getName(arg_name)
    msg = getGreeting(name)
    print(f"name: {name} ,msg: {msg}")

prtShow("홍길동")

