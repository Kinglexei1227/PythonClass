# 주문 정보 입력 (모두 문자열로 입력받음)
drink = input("음료를 선택하세요 (coffee/latte/juice): ")
size = input("크기를 선택하세요 (small/medium/large): ")
membership = input("멤버십이신가요? (yes/no): ")

# Happy Scenario 가정
# 음료 기본 가격 설정
if drink == "coffee" :
    price = 3000
elif drink == "latte" :
    price = 4000
elif drink == "juice" :
    price = 3500

# 사이즈 크기 추가 요금 설정
if size == "small" :
    extra_price = 0
elif size == "medium" :
    extra_price = 500
elif size == "large" :
    extra_price = 1000

# 할인 금액 설정 (멤버십 유무)
if membership == "yes" :
    discount = (price + extra_price) * 0.1
else:
    discount = 0

# 최종 결제 금액 계산
total_price = price + extra_price - discount

# 무료 샷 제공 여부
if (drink == "coffee" or drink == "latte") and size == "large" and membership == "yes":
    msg = "무료 샷이 제공됩니다!"
else :
    msg = ""

# 결과 출력
print(f"\n기본 가격: {price}원")
print(f"크기 추가 요금: {extra_price}원" if extra_price > 0 else "크기 추가 요금: 없음")
print(f"할인 적용: -{int(discount)}원" if discount > 0 else "할인 적용: 없음")
print(f"최종 결제 금액: {int(total_price)}원")

if msg:
    print(msg)