# 키보드로부터 두 개의 정수를 입력 받아 저장
input_value1 = int(input("첫 번째 입력 값: "))
input_value2 = int(input("두 번째 입력 값: "))

# 메뉴 출력
menu =  """----------------------
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
----------------------"""
print(menu)

# Test - 1
#print(f"{input_value1} + {input_value2} = {input_value1 + input_value2}")

# 메뉴 선택
sel_menu = int(input("메뉴를 선택 하세요!"))

#선택된 메뉴에 따른 연산 실시
result = 0
if sel_menu == 1:
    result = input_value1 + input_value2
elif sel_menu == 2:
    result = input_value1 - input_value2
elif sel_menu == 3:
    result = input_value1 * input_value2
elif sel_menu == 4:
    result = input_value1 / input_value2
else:
    result = "잘못된 입력 입니다."

#결과 값 출력
print(result)