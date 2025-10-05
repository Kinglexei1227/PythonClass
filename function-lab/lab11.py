# 여러 개의 정수와 함께 다양한 옵션(키워드 인자)을 입력 받아,
# 조건에 따라 합계를 계산하는 함수를 작성

def add_numbers(*args, **kwargs):
    sum = 0
    for num in args:
        sum += num
    
# 결과들 출력
add_numbers(1, -2, 2, -3)

add_numbers(1, -2, 2, -3, abs = True, only_even = True)

add_numbers(1, 2, 2, 3, 3, 4, unique = True)

add_numbers(1, 2, 3, round=True)

