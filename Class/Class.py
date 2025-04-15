# Truthy, Falsy 예제
temp_1 = 1  # 정수형 변수
temp_2 = -1 # 정수형 변수
temp_3 = 0  # 정수형 변수
temp_4 = -0 # 정수형 변수

if temp_1:        # 1 -> Truthy 값
    print("참")   # 출력값
else:
    print("거짓")
    
if temp_2:        # -1 -> Truthy 값
    print("참")   # 출력값
else:
    print("거짓")

if temp_3:        # 0 -> Falsy 값
    print("참")
else:
    print("거짓") # 출력값

if temp_4:        # -0 -> Falsy 값
    print("참")   
else:
    print("거짓")  # 출력값