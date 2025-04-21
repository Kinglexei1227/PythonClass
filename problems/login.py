# 로그인 시스템

ID = "admin"
PW = "1234"

# 사용자로 부터 ID , PW 입력

input_id = input("ID 입력: ")
input_pw = input("PW 입력: ")

# 올바른 아이디 입력때 까지 반복: while문 사용 (최대 5회)
while True :
    if input_id == ID and input_pw == PW :
        print("로그인 성공!")
        break
    else:
        print("ID 또는 PW가 잘못되었습니다.")
        for i in range(5, 1, -1):
            print(f"남은 시도: {i}")
            break