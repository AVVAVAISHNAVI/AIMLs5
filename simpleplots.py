import matplotlib.pyplot as plt
import numpy as np

# Bar Plot
x = ['A', 'B', 'C', 'D']
y = [10, 20, 30, 40]
plt.bar(x, y)
plt.title('Bar Plot')
plt.show()

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('Histogram')
plt.show()

# Box Plot
data = np.random.randn(100)
plt.boxplot(data)
plt.title('Box Plot')
plt.show()
