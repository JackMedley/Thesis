from matplotlib import pyplot as plt
import numpy as np
from math import sqrt, atan, tan, asin

# Bare integrand
def f(x):
	return 150.0 * x**2 * asin(x**2)

# Integrand integrand
def g(x):
	return 150.0 * (5 ** 0.2) * asin((25.0 * x) ** 0.4) / (x ** 0.4)

# Integration details
a, b, N = 0, 0.5, 1e5

# Uniform sampling
Sum  = 0.0
Sum2 = 0.0
for x in np.random.uniform(a, b, N):

	# Evaluate integrand
	temp = f(x)

	# Keep track of sum and sum of squares
	Sum  += temp
	Sum2 += temp ** 2

# print 'uniform'
# fbar  = (b - a) * Sum  / N
# f2bar = (b - a) * Sum2 / N
# print fbar, '\pm', sqrt(abs(f2bar - (fbar ** 2))), '&', abs(fbar - 0.943034097924532)

# Importance sampling
Sum  = 0.0
Sum2 = 0.0

for x in np.random.uniform(0.0, 0.5 ** 5 / 25.0, N):

	# Evaluate integrand
	temp = g(x)

	# Keep track of sum and sum of squares
	Sum  += temp
	Sum2 += temp ** 2

# Return averages
fbar  = (0.5 ** 5) / 25.0
f2bar = (0.5 ** 5) / 25.0

fbar  *= Sum  / N
f2bar *= Sum2 / N

print fbar, '\pm', sqrt(abs(f2bar - (fbar ** 2)) / (25.0*N)), '&', abs(fbar - 0.943034097924532)
