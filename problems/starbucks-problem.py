# 별다방에서 고객의 주문을 받아 음료 가격과 혜택을 계산하는 프로그램을 작성.

#각 음료에 대한 가격
coffee = 3000
latte = 4000
juice = 3500

# 크기 추가 요금
small = 0
medium = 500
large = 1000

# 음료와 크기, 멤버십 유무

input_drink = input("음료를 선택하세요 (coffee/latee/juice): ")
input_size = input("크기를 선택하세요 (small/medium/large): ")
input_membership = input("멤버십이신가요? (yes/no): ")

# 경우에 따라 적용 (if문)
if input_drink == "coffee" :
    drink_amount = coffee
elif input_drink == "latte" :
    drink_amount = latte
elif input_drink == "juice" :
    drink_amount = juice
else :
    print("잘못된 입력입니다.")
    exit()

# 사이즈에 따라 추가가격 적용
if input_size == "small" :
    size_amount = small
elif input_size == "medium" :
    size_amount = medium
elif input_size == "large" :
    size_amount = large
else :
    print("잘못된 입력입니다.")
    exit()

# 경우에 따른 계산수식
amount = drink_amount + size_amount

# 할인율 계산
discount_amount = 0 # 할인율
if input_membership == "yes" :
    discount_amount = amount * 0.1

# 최종 결제 금액
total_amount = amount - discount_amount

# 결과값 출력
print(f"기본 가격: {drink_amount}")
print(f"크기 추가 요금:{size_amount}")
print(f"할인 적용: -{int(discount_amount) if input_membership == "yes" else "없음"}")
print(f"최종 결제 금액:{int(total_amount)}")

# 멤버십 유무
if input_membership == "yes" :
    print("무료 샷이 제공됩니다!")