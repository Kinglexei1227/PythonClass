import matplotlib.pyplot as plt

# 값
x = [val for val in range(0, 21)]
y = [val*2 for val in x]
print(x)
print(y)

# 그래프 종류 선택
plt.plot(x, y) # 선형 그래프

# 그래프 꾸미기

# 그래프 출력
plt.show()
