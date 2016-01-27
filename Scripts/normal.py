from matplotlib import pyplot as plt
import numpy as np
from math import sqrt

def f(x):
	return np.exp(-3*abs(x))
	# return 3.0 * np.exp(- x**2 / 2.0)

if False:
	mu, sigma = 0, 0.5
	s = np.random.normal(mu, sigma, 1000)
	count, bins, ignored = plt.hist(s, 30, normed=True)
	plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
	plt.show()

else:
	# No. of samples
	N = 1e1

	# Domain
	a, b = -5, 5

	# Uniform sampling
	Sum  = 0.0
	Sum2 = 0.0
	for x in np.random.uniform(a, b, N):
		temp = f(x)
		Sum  += temp
		Sum2 += temp ** 2

	print 'uniform'
	fbar  = (b - a) * Sum  / N
	f2bar = (b - a) * Sum2 / N
	print fbar, ',', sqrt(abs(f2bar - fbar ** 2))

	# Importance sampling
	Sum  = 0.0
	Sum2 = 0.0
	mu, sigma = 0, 1
	for x in np.random.normal(mu, sigma, N):

		temp = f(x) / (np.exp(- (x ** 2) / (2.0 * sigma ** 2)) / (sigma * sqrt(2.0 * np.pi)))

		# Keep track of sum and sum of squares
		Sum  += temp
		Sum2 += temp ** 2

	# Return averages
	print 'IS'
	fbar  = Sum  / N
	f2bar = Sum2 / N
	print fbar, ',', sqrt(abs(f2bar - fbar ** 2))

