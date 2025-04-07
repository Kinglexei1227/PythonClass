# 주어진 점수로 등급을 부여하는 프로그램
# 사용자로부터 점수를 입력 받는다.
record = int(input("점수를 입력하세요: "))
# 사용자로부터 받은 점수를 등급으로 환산산
if record >= 90:
    print("A")
elif record >= 80:
    print("B")
elif record >= 70:
    print("C")
elif record >= 60:
    print("D")
else:
    print("F")

# a, b, c = 5, 6, 10
# result = a < b < c # True, a는 b보다 작고 b는 c보다 작다.
# print(result)

# x = 20
# if 10 < x < 30:
#     print("x는 10과 30 사이에 있습니다.") # 출력

# y = 15
# if 5 < y <= 20:
#     print("y는 5 초과 20 이하입니다.") # 출력
    
# print(2 < 3 < 5 < 6 < 7) # True

# y = 1

# if 5 < y <= 20:
#     pass

# if y > 5 and y <= 20:
#     pass