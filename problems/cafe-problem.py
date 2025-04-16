######## 가격 설정 ########### 
coffee = 3000
latte = 4000
juice = 3500

large = 1000
medium = 500
small = 0
##############################

# 메뉴와 크기 입력 + 멤버쉽 
input_menu = input('음료를 선택하세요 (coffee/latte/juice) : ')
input_size = input('크기를 선택하세요 (small/medium/large) : ')
input_membership = input('멤버쉽이신가요? (yes/no) : ')

# 경우에 따라 가격 적용 
if input_menu == 'coffee' :
    menu_amount = coffee
elif input_menu == 'latte' :
    menu_amount = latte
elif input_menu == 'juice' :
    menu_amount = juice
else : 
    print('잘못된 입력입니다.')
    exit()

# 경우에 따라 크기 추가 요금 적용
if input_size == 'large' :
    extra_amount = large
elif input_size == 'medium' :
    extra_amount = medium
elif input_size == 'small' :
    extra_amount = small
else : 
    print('잘못된 입력입니다.')
    exit()
    
# 할인 전 전체 금액
amount = menu_amount + extra_amount

# 할인율 계산 
discount_amount = 0
if input_membership == 'yes' :
    discount_amount = amount * 0.1
    
    
# 최종 결제 금액 설정 
total_amount  = amount - discount_amount

print(f"기본가격: {menu_amount}")
print(f"크기 추가 요금: {extra_amount}")
print(f"할인 적용: { discount_amount if input_membership == "yes" else "없음"}")
print(f"최종 결제 금액: {total_amount}")

if input_membership == "yes" and (input_menu == "latte" or input_menu == "coffee") and input_size == "large":
    print("샷 추가")   
    