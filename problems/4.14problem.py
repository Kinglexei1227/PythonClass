# 별다방 주문 처리 시스템 (Happy Scenario)

# 사용자로부터 주문 입력받기
drink = input("음료를 선택하세요 (coffee/latte/juice): ")
size = input("크기를 선택하세요 (small/medium/large): ")
membership = input("멤버십이신가요? (yes/no): ")

# 음료 기본 가격 결정
if drink == "coffee":
    drink = 3000
elif drink == "latte":
    drink = 4000
elif drink == "juice":
    drink = 3500
# 크기별 추가 요금
if size == "small":
    size = 0
elif size == "medium":
    size = 500
elif size == "large":
    size = 1000
# 기본 + 추가 요금 계산
amount = drink + size
# 멤버십 유무 판별(있을시 10% 할인)
if membership == "yes":
    discount_amount = amount * 0.1
else:
    discount_amount = 0
# 멤버십 고객이면서 커피/라떼 + large 사이즈일 경우 무료 샷 제공
if (drink == "coffee" or drink == "latte") and membership == "yes" and size == "large" :
    print("무료 샷이 제공됩니다!")

total_amount = amount - discount_amount
# 결과 출력
print(f"기본 가격: {drink}")
print(f"크기 추가 요금: {size}")
print(f"할인 적용: {discount_amount}")
print(f"최종 결제 금액: {total_amount}")
