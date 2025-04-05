#사용자로부터 정수와 실수를 각각 하나씩 입력받아 두수의 차를 계산하고, 결과값과 그 자료형을 출력하는 프로그램 작성.

# 정수 입력, 실수 입력
input_value1 = int(input("정수를 입력하세요: "))
input_value2 = float(input("실수를 입력하세요: "))
#두 수의 차(뺄셈)를 계산
#result = input_value1 - input_value2
substract = input_value1 - input_value2

#결과값과 결과값의 자료형을 print 함수로 출력
print(f"결과 값:{substract}, 자료형:{type(substract)} ")