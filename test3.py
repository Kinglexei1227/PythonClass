# 사용자로부터 메뉴 번호를 입력받아 
# 해당 도형의 면적을 계산하는 프로그램을 작성한다.

#  1. 원의 면적 계산 함수
def circle():
    radius = int(input("반지름을 입력하세요: "))
    return radius ** 2 * 3.14 # 원의 면적 수식 = π × 반지름² (π는 3.14로 고정)

#  2. 삼각형의 면적 계산 함수
def triangle():
    length = int(input("밑변을 입력하세요: "))
    height = int(input("높이를 입력하세요: "))
    return (length * height) / 2 # 삼각형의 면적 수식 = (밑변 × 높이) ÷ 2

#  3. 사각형의 면적 계산 함수
def rectangle():
    width = int(input("가로를 입력하세요: "))
    height = int(input("세로를 입력하세요: "))
    return (width * height) # 사각형의 면적 수식 = 가로 × 세로

# 사용자가 선택한 메뉴 번호에 따라 
# 필요한 값을 입력받고 면적을 계산한다.
print("""
      [도형 면적 계산기]
      1. 원
      2. 삼각형
      3. 사각형
      """)

menu =int(input("메뉴를 선택하세요: "))

# 메뉴입력값에 따라 실행되는 함수들
result = ""
if menu == 1:
    result = f"원의 면적은 {circle()}"
elif menu == 2:
    result = f"삼각형의 면적은 {triangle()} 입니다."
elif menu == 3:
    result = f"사각형의 면적은 {rectangle()} 입니다."
    
else:
    result = "잘못된 선택입니다."
    
print(result)
