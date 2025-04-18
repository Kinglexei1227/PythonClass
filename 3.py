# 비밀번호 검증기 프로그램

# 사용자로 부터 입력받은 비밀번호가 8자 이상, 1개 이상의 숫자, 1개 이상의 대문자 가 반드시 포함

password = input("비밀번호를 입력하세요: ")
if len(password) >= 8 :
    print("비밀번호 길이가 충분합니다.")
else :
    print("비밀번호가 너무 짧습니다.")

has_number = False
for char in password :
    if char.isdigit():
        has_number = True
        break # 숫자가 확인되면 더 이상 반복하지 않습니다. 

has_uppercase = False
for char in password :
    if char.isupper():
        has_uppercase = True
        break # 대문자가 확인되면 더 이상 반복 X