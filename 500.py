import matplotlib.pyplot as plt

# 값
x = [val for val in range(0, 21)]
y = [val*2 for val in x]
print(x)
print(y)

# 그래프 종류 선택
plt.scatter(x, y, color='red', marker="*") # 산점도 그래프

# 그래프 꾸미기
plt.xlabel("X 축")
plt.ylabel("Y 축")
plt.title("선형 그래프")
plt.grid(True)

# 그래프 출력
plt.show()
