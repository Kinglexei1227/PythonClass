# 고객 등급을 판별하는 프로그램 작성.

# 고객으로 부터 입력값 받기
consume_cost = int(input("총 구매 금액: "))
return_num = int(input("총 반품 횟수: "))
buy_num = int(input("총 구매 횟수: "))
monthly = int(input("가입 개월 수: ")) 

# 예외 처리
if buy_num == 0:
    print('''
오류: 구매 횟수가 0입니다. 반품율을 계산 할수 없습니다.
프로그램을 종료합니다.''')
    exit()
elif return_num > buy_num :
    print('''
오류: 반품 횟수가 구매 횟수보다많을 수 없습니다.
프로그램을 종료합니다.''')
    exit()
# 반품률
return_rate = (return_num / buy_num * 100) #반품률 계산식: (반품 횟수 / 구매횟수 X 100)

# 위험 고객 조건 : 다음 조건 중 하나라도 해당되면 위험 고객
# 조건 1 반품률 >= 50% 
# 조건 2 가입 개월 수가 3개월 이하이고 구매 금액이 10000원 이하
# 조건 3 반품 횟수가 1회 이상
if return_rate >= 50 or monthly <= 3 or consume_cost <= 10000 or return_num >= 10: # if 1 or 2 or 3 (알고리즘)
    print(f'''
반품률: {return_rate:.1f}%
결과: 위험 고객''')



# 우수 고객 조건 : 위험 고객이 아닌 경우 중 아래 모든조건을 만족:
# 구매 금액이 200만 원 이상
# 반품률 <= 10%
# 구매 횟수 >= 30회
# 가입 개월 수 >= 12개월 
elif consume_cost >= 2000000 and return_rate <= 10 and buy_num >= 30 and monthly >= 12: # if 1 and 2 and 3 and 4 (알고리즘)
    print(f'''
반품률: {return_rate:.1f}%
결과: 우수 고객''')
    
# 위 조건에 해당하지 않으면 일반 고객으로 분류
else:
    print(f'''
반품률: {return_rate:.1f}%
결과: 일반 고객''')
