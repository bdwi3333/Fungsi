from matplotlib import pyplot as plt
from numpy.random import normal
from numpy import mean, std
from scipy.stats import norm

sample = normal(loc=50, scale=5, size=1000)

plt.figure(figsize=(5,4))
plt.hist(sample, bins=10, density=True)
plt.show()
