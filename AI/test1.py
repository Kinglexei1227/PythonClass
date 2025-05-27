import matplotlib.pyplot as plt

# 데이터를 준
x = range(-10, 11)
y = [ val**2 for val in x]

# 그래프 종류 선택 후 드로잉
plt.plot(x, y)

plt.title("A graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)

# 그래프 출력
plt.show()