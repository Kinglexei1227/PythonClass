import matplotlib.pyplot as plt


x = [ val for val in range(-10, 11)]
y = [val**2 for val in x]

plt.plot(x, y, color = "red")
plt.plot(x, x, marker='o')

plt.legend()
plt.title("A graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()