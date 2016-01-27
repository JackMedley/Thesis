import matplotlib.pyplot as plt
import numpy as np
from math import log, atan, tan

# Uniform
x = np.random.uniform(1.5, 20.0, 1000)

# Exponential
# x = [- log(1 - y) for y in x]

# Cauchy
# x = [atan(y - 5.0) for y in x]
# x = [ atan(y - 5.0) / np.pi - 0.5 for y in x]

# Inverse sampling generation
x = [5.0 + tan(np.pi * (y - 0.5)) for y in x]

hist, bins = np.histogram(x, bins=50)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)

plt.yscale('log')
plt.xlim([-100.0, 100.0])
# plt.ylim([1e-3, 5.0])
plt.show()

