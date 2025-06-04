# 메뉴 리스트 인덱스 읽기

menus = ["피자", "파스타", "샐러드", "스시", "버거"]

# 사용자로부터 인덱스 입력받기
input_index = int(input("메뉴의 인덱스를 선택하세여 (0부터 시작): "))

if 0 <= input_index <= len(menus):
    print(f"선택된 메뉴: {menus[input_index]}")
else:
    print("유효하지 않은 선택입니다.")