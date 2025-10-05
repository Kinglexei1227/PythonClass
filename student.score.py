# 딕셔너리 선언
std_data = {'id': 0, 'name': "", 'korean_score': 0, \
            'math_score' : 0, 'english_score': 0, 'total' : 0, 'avg': 0.0}

# 메뉴 반복 출력
while True:
    print('''
===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료
''')
    
    # 메뉴 선택
    menu_input = int(input("메뉴 선택 (1~5): "))

    # 조건에 따라 기능
    if menu_input == 1:
        student_id_input = int(input("학번 입력: "))
        name_input = input("이름 입력 :")
        korean_input = int(input("국어 성적 입력: "))
        english_input = int(input("영어 성적 입력: "))
        math_input = int(input("수학 성적 입력: "))

        # 점수 총합
        total = korean_input + english_input + math_input
        # 평균 점수
        avg = (korean_input + english_input + math_input) / 3
        # 딕셔너리 저장
        std_data['id'] = student_id_input
        std_data['name'] = name_input
        std_data['korean_score'] = korean_input
        std_data['english_score'] = english_input
        std_data['math_score'] = math_input
        std_data['total'] = total
        std_data['avg'] = avg
        print("성적이 저장되었습니다.")

    elif menu_input == 2:
        print(f"[ 전체 학생 성적]")
        print(f"{std_data}")

    elif menu_input == 3:
        user_input = int(input("조회할 학번 입력:"))
        if user_input == std_data["id"]:
            print(f'''
[ 학생 정보 ]
학번: {std_data["id"]}
이름: {std_data["name"]}
국어: {std_data["korean_score"]}
영어: {std_data["english_score"]}
수학: {std_data["math_score"]}
합계: {std_data["total"]}
평균: {std_data["avg"]}
''')
        else:
            print("해당 학번의 학생 정보가 없습니다.")

    elif menu_input == 4:
        sdt_delete = int(input(""))

    elif menu_input == 5:
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("잘못된 입력값입니다.")