'''
사용자가 입력한 상품 가격에 따라 할인율을 적용하여 할인금액과 최종 결제 금액을 계산하는 프로그램.

10만 원 이상구매시 -> 10%(0.1) 할인
5만 원 이상 10만 원 미만 구매 시 -> 5%(0.5) 할인
5만 원 미만 구매 시 할인 없음
'''

# 사용자로 부터 상품 가격을 입력 받는다 (정수형)
price = int(input("상품 가격을 입력하세요: "))

# 조건에 따라 할인율을 설정 (if조건문)
if price >= 100000:
    discount_rate = 0.1 # 10만원 이상 구매시 10% 할인
elif price >= 50000:
    discount_rate = 0.05 # 5만원 이상 구매시 5% 할인
else:
    discount_rate = 0 # 그외 할인 불가

# 할인 금액 계산식 (정수로 변환하여 소수점 제거)
discount_amount = int(price * discount_rate)

# 최종 결제 금액 계산식 (상품가격 - 할인 금액)
total_amount = price - discount_amount

# 결과 값을 출력
print(f"할인율: {int(discount_rate*100)}%")
print(f"할인 금액: {discount_amount}원")
print(f"최종 결제 금액: {total_amount}원")