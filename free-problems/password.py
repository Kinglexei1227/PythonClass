# 비밀번호 검증기

# 사용자로부터 비밀번호 입력 받기
password = input("비밀번호를 입력하세요: ")


# 비밀번호에 대문자 1개 이상, 숫자 1개 이상 포함되어 있는지 확인
has_digit = False
has_upper = False
for char in password :
    if char.isdigit() :
        has_digit = True
    if char.isupper() :
        has_upper = True

# 두 조건을 만족하고 비밀번호(문자열) 길이가 8자 이상일시 비밀번호 안전문 출력
if has_digit and has_upper and len(password) >= 8 :
    print("비밀번호가 안전합니다.")
else :
    print("비밀번호가 안전하지 않습니다.")
