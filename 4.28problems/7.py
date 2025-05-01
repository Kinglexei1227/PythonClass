# 별 다이아몬드 출력

num = 5
# 피라미드 출력
for i in range(1 , num + 1):
    print(" " * (num - i) , "*" * (2 * i - 1))
# 역 피라미드 출력
for i in range(num -1, 0 , -1):
    print(" " * (num - i) , "*" * (2 * i - 1))