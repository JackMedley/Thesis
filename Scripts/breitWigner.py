# Importance sampling

from matplotlib import pyplot as plt
from math import sqrt
import cmath
import numpy as np

X = np.linspace(0.0, 20.0, 200, endpoint=True)

# Integrand
# fn2 = 1.0 / ((X - 91.0) ** 2 + (91.0 * 2.085) ** 2)
fn2 = 1.0 / ((X - 5.0) ** 2 + 1)

plt.rc('text', usetex=True)

# Uniform PDF
# x = [-10,-5, 5, 10]
# y = [0.0, 0.0, 0.1, 0.0]

# Plot Integrand
plt.plot(X, fn2, linewidth=3)

# Plot PDF
# plt.plot(X, fn3, linewidth=3)

# Sort out axes
# plt.xlim([-6, 6])
plt.ylim([1e-3, 5.0])

# Sort out labels
plt.xlabel(r'$p_Z^2$', size=14)
plt.ylabel(r'$\Bigg|\frac{1}{p_Z^2 - M_Z^2 + i\Gamma_ZM_Z}\Bigg|^2$', size=14)

plt.yscale('log')

# Plot
# plt.show()
plt.savefig('breitWigner.pdf')

