# 로그인 시스템

# 조건 -> (올바른 입력값) ID = admin , PW = 1234

correct_id = "admin"
correct_pw = "1234"

# 로그인 횟수 초기화
attempt = 0

# while 문으로 로그인 시도 횟수를 제한(최대 5회).
while attempt < 5:
    ID = input("ID 입력: ")
    PW = input("PW 입력: ")
# 입력값이 올바르면 "로그인 성공!" 출력 후 종료.
    if ID == "admin" and PW == "1234":
        print("로그인 성공!")
        break
# 틀릴경우 시도 횟수를 1 증가 밑 오류 메세지 출력
    else:
        attempt += 1
        remain = 5 - attempt
        print(f"ID 또는 PW가 잘못되었습니다. (남은시도: {remain})")
    

# 5회 초과 시 "계정이 잠금되었습니다." 출력 후 종료.
        if remain == 0:
            print("계정이  잠금되었습니다.")