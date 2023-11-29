import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,6,14])
ypoints = np.array([10,50,10])

plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints, color='red')
plt.xlim([0,15])
plt.ylim([0,50])
plt.show()
