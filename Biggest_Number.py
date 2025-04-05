# 사용자로부터 세 개의 정수 숫자를 입력받고,
# 이 중 가장 큰 숫자를 찾아 출력하는 프로그램을 작성.

# 사용자로부터 세 개의 정수 숫자를 입력받습니다.
num1 = int(input("첫 번째 숫자를 입력하세요:"))
num2 = int(input("두 번째 숫자를 입력하세요:"))
num3 = int(input("세 번째 숫자를 입력하세요:"))

# 입력받은 숫자들 중 가장 큰 숫자를 판별합니다.
if num1 >= num2 and num1 >= num3 :
    ANS = num1
elif num2 >= num1 and num2 >= num3 :
    ANS = num2
else :
    ANS = num3

# 가장 큰 숫자를 출력합니다
print("가장 큰 숫자는",ANS ,"입니다")