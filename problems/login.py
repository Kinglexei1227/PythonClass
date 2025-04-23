# 로그인 시스템

ID = "admin"
PW = "1234"

# 로그인 시도 횟수 초기화
attempt = 0

# 최대 5번까지 로그인 시도 허용
while attempt < 5:
    # 사용자로부터 ID와 비밀번호 입력받기
    user_id = input("ID 입력: ")
    user_pw = input("PW 입력: ")    
    # 입력값이 올바른 경우 -> 로그인 성공
    if user_id == ID and user_pw == PW :
        print("로그인 성공!")
        break
    # 입력값이 틀린 경우 -> 시도 횟수 증가및 오류 메시지 출력
    else :
        attempt += 1   # 실패 횟수 1 증가
        remain = 5 - attempt   # 남은 시도 횟수 계산
        print(f"ID 또는 PW가 잘못되었습니다. (남은 시도:{remain})")                                    
    # 5회 초과 시 계정 잠금 메시지 출력
        if remain == 0 :
            print("계정이 잠금되었습니다.")
    
        # 오류 메시지와 함께 남은 횟수 안내