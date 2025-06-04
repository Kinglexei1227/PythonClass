# 패스워드 생성기

# 랜덤 설정
import random
# 랜덤 비밀번호 함수 정의
def generate_password(length):
    # 대문자, 소문자, 숫자를 포함한 문자열 정의
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower() # 대문자를 소문자로 변환
    digits = '0123456789'
    all_characters = uppercase_letters + lowercase_letters + digits

    # 패스워드 초기화
    password = ""

    # 지정된 길이만큼 랜덤 문자 선택
    for _ in range(length):
        password += random.choice(all_characters) # 랜덤 문자를 패스워드에 추가

    # 생성된 패스워드 반환
    return password

# 함수 호출하여 패스워드 생성
generated_password = generate_password(8)
print(generated_password)