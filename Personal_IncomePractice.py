#사용자로부터 소득 금액을 입력받아 소득세를 계산하는 프로그램을 만듭니다
income = int(input("소득 금액을 입력하세요:"))

#소득세 계산 함수
def calculate_tax(income) : 
    if income <= 10000 : #첫 1만 달러의 소득(income)에는 10%의 세율이 적용됩니다.
        return income / 10
    elif 10000 < income <= 20000 : #1만달러를 초과, 2만달러 이하의 소득에는 초과 금액의15%의 세율 적용하고,
        #첫 1만 달러의 세금인 1천 달러를 더합니다.
        return (income - 10000) * 0.15 + 1000
    else : # 2만달러를 초과하는 소득에는 초과금액의 20%세율적용하고, 
        #앞선 구간의 세금인 2천 5백 달러를 더합니다. 
        return (income - 20000) * 0.2 + 2500
    
A = calculate_tax(income)   
print(f"소득세는 {A} 입니다")
