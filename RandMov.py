import random
import matplotlib.pyplot as plt

x, y = 0, 0
x_vals, y_vals = [x], [y]

for _ in range(1000):
    dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
    x += dx
    y += dy
    x_vals.append(x)
    y_vals.append(y)

plt.plot(x_vals, y_vals)
plt.title('Random Movement')
plt.show()
