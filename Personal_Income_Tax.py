# 이 프로그램은 사용자로부터 소득 금액을 입력받아소득세를 계산합니다.

income = int(input("소득 금액을 입력하세요:"))

def calculate_tax(income) :
    if income <= 10000 :
        print("소득세는", income /10,"입니다다")
    elif 10000 <= income <= 20000 :
        print(f"소득세는 {(income - 10000)* 0.15 + 1000} 입니다")
    else :
        print(f"소득세는 {(income - 20000)* 0.2 + 2500} 입니다")
        
        
        
        

calculate_tax(income)
        