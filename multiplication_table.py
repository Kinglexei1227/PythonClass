# 구구단 프로그램: 2단부터 9단까지의 구구단을 출력합니다.

for factor in range(2, 10): # 2단부터 9단까지의 단을 위한 반복문 시작
    for multiplier in range(1, 10): # 각 단에 대해 1부터 9까지 곱할 숫자를 위한 반복문 시작
        print(factor, "X", multiplier, "=", factor*multiplier) # 현재 단(dan)과 숫자(num)의 곱을 출력
    print("----------") # 하나의 단이 끝나면 구분선을 출력
        