# 사용자로부터 섭씨 온도를 입력받아 화씨 온도로 변환하는함수를 작성하고,
# 변환된화씨 온도를 출력하는 프로그램을 작성하세요.

# 화씨 온도는 섭씨 온도에 9/5를 곱한 후 32를 더해 계산합니다
# 사용자에게 섭씨 온도를 입력받습니다.
celsius = int(input("섭씨 온도를 입력하세요:"))
# 섭씨를 화씨로 변환하는 함수를 작성합니다.
fahrenheit = (celsius * 9/5) + 32
# 변환된 화씨 온도를 출력합니다.
print("화씨 온도는", fahrenheit, "입니다")