# 가상 주식 거래 시뮬레이터

# 사용자로부터 정보를 입력받기

first_capital = int(input("초기 자본금을 입력하세요: "))
stock_amount = int(input("주식 가격을 입력하세요: "))
stock = int(input("구매할 주식 수를 입력하세요: "))
stock_sell = int(input("판매할 때의 주식 가격을 입력하세요: "))

# 각 계산식

total_cost = stock_amount * stock # 총 구매 비용 계산
remain_capital = first_capital - total_cost # 남은 자본금 계산
cost = stock_sell * stock - total_cost # 판매 예상 이익 혹은 손실 계산식


# 결과 출력'
print(f"구매 후 남은 자본금:{remain_capital}")
print(f"예상 이익:{cost} ")

# 이익 혹은 손실시 출력값
if cost > 0 :
    print("예상되는 이익입니다.")
else :
    print("예상되는 손실입니다.")