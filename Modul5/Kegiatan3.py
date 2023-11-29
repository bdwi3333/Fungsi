import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3,12,5,1])
y2 = np.array([6,10,7,11])

plt.plot(y1, label='Garis 1')
plt.plot(y2, label='Garis 2')

plt.title('Plot Dua Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.legend()
plt.show()
