'''
별다방에서 고객의 주문을 받아 음료 가격과 혜택을 계산하는 프로그램

고객으로부터 정보 입력
음료, 크기, 멤버십 여부 입력 (모두 소문자로)
'''
drink = input("음료를 선택하세요 (coffee/latte/juice): ")
size = input("크기를 선택하세요 (small/medium/large): ")
membership = input("멤버십이신가요? (yes/no): ")

# 음료 기본 가격 결정
price = 0
# 가격 계산
if drink == "coffee" :
    price += 3000
elif drink == "latte" :
    price += 4000
else :
    price += 3500
# 크기 추가 요금
size_price = 0
if size == "medium" :
    size_price += 500
elif size == "large" :
    size_price += 1000
# 멤버십 혜택
if membership == "yes": # 
    discount_price = (price + size_price) / 10
    discount = price - discount_price
    if drink == "coffee" or drink == "latte" : 
        if size == "large" : # 무료 샷 제공 조건
            print("무료 샷이 제공됩니다!")
        else:
            discount_price = 0
# 출력 결과

print(f'''
기본 가격: {price}
크기 추가 요금: {size_price}
할인 적용: -{discount_price}
최종 결제 금액: {discount}''')