# Importance sampling

from matplotlib import pyplot as plt
from math import sqrt, asin
import numpy as np

X = np.linspace(0.0, 1.0, 1000, endpoint=True)

# Integrand
# fn2     = 1.5*np.exp(-2.0*abs(X))
# fn2     = np.exp(-3*abs(X))
fn2     = [150.0 * x**2 * asin(x**2) for x in X]

# Normal PDF
# mu    = 0.0
# sigma = 0.5
# fn3   = np.exp(-(X - mu) ** 2 / (2.0 * sigma ** 2)) / (sigma * sqrt(2.0 * np.pi))
fn3 = ((5.0 / (0.5 ** 5)) * X ** 4)

# Uniform PDF
x = [-10, 0, 0.5, 10]
y = [0.0, 0.0, 2.0, 0.0]

if True:
	# Plot Integrand
	plt.plot(X, fn2, linewidth=3)

	# Plot normal PDF
	plt.plot(X, fn3, linewidth=3)

	# Plot uniform PDF
	plt.step(x, y, linewidth=3)

else:
	plt.plot(ratio, linewidth=3)

# Sort out axes
plt.xlim([-0.1, 0.6])
plt.ylim([0, 10.0])

# Sort out labels
plt.xlabel('x', size=14)
plt.ylabel('f(x)', size=14)

# Plot
# plt.show()
plt.savefig('importanceSampling.pdf')

