#사용자로부터 두 개의 정수 숫자를 입력 받고, 그 합, 차, 곱, 나눗셈의 결과를 출력하는 프로그램을 작성하세요.
#사용자에게 두 정수 숫자를 입력 받습니다.

#첫 번째 숫자를 입력 받는다.
num1 = float(input("첫 번째 숫자를 입력하세요"))

#두 번째 숫자를 입력 받는다.
num2 = float(input("두 번째 숫자를 입력하세요"))

#입력받은 숫자들의 합, 차, 곱, 나눗셈, 결과를 계산합니다.
sum = num1 + num2
minus = num1 - num2
multiplier = num1 * num2
divide = num1 / num2
#계산된 결과를 출력합니다.
print(sum)
print(minus)
print(multiplier)
print(divide)