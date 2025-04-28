# 반복
while True:
    # 메뉴 출력
    print("""
        ----메 뉴----
        1. 합계
        2. 평균
        3. 지수
        4. 종료
          """)
    # 메뉴 입력
    input_num = int(input("메뉴를 선택 하세요"))
    
    # 입력된 메뉴에 따라 프로그램 실행
    # 1번 합계
    if input_num == 1:
        input_num1 = int(input("첫 번째 값을 입력하세요: "))
        input_num2 = int(input("두 번째 값을 입력하세요: "))
        print(f"합계 : {input_num1 + input_num2}")
    # 2번 평균
    elif input_num == 2:
        input_num1 = int(input("첫 번째 값을 입력하세요: "))
        input_num2 = int(input("두 번째 값을 입력하세요: "))
        input_num3 = int(input("두 번째 값을 입력하세요: "))
        print(f"합계 : {(input_num1 + input_num2 + input_num3) / 3}")
    # 3번 지수
    elif input_num ==3:
        input_num1 = int(input("밑수를 입력하세요: "))
        input_num2 = int(input("지수를 입력하세요: "))
        print(f"지수: {input_num1 ** input_num2}")
    # 4번 종료
    elif input_num ==4:
        print("프로그램 종료.")
        break
    # 5번 예외처리
    else:
        print("1~4 사이 정수를 입력하세요.")