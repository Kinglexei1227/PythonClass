# matplotlib의 pyplot 모듈을 plt라는 이름으로 임포트
import matplotlib.pyplot as plt

# 1. 데이터 준비
# x는 -10부터 10까지 정수 리스트
x = [val for val in range(-10, 11)]
# y는 각 x 값의 제곱(x^2)
y = [val**2 for val in x]

# 2. 그래프 그리기
# 선형 그래프(Line graph)를 그린다. x축: x 값, y축: x^2 값
plt.plot(x, y)

# 3. 그래프 꾸미기
plt.title("X^2 Graph")    # 그래프 제목
plt.xlabel("x")           # x축 라벨
plt.ylabel("x^2")         # y축 라벨

# 4. 그래프 출력
plt.show()