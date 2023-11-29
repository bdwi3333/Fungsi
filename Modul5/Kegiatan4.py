import matplotlib.pyplot as plt
import numpy as np

x = [6,4,10,9,6]
y = [3,7,2,8,5]

plt.title('Scatter plot')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.scatter(x, y)
plt.show()
