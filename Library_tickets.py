# 도서관에서 나이에 따라 다양한 이용권을 제공하는 프로그램을 작성
# 사용자의 나이정보를 입력받아, 
# 해당 사용자에게 적합한 도서관 이용권을 판별하는 프로그램을 작성
# 사용자의 나이를 입력받는 프로그램 작성
Age = int(input("사용자의 나이를 입력해주세요: "))
# 입력받은 나이에 따라 적합한 도서관 이
if Age <= 12 :
    print("어린이 이용권을 사용할 수 있습니다.")
elif 12 < Age <= 18 :
    print("청소년이용권을 사용할 수 있습니다.")
else :
    print("성인이용권을 사용할 수 있습니다.")
    