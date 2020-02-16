## Exercise 1
# import numpy as np

class Ploy:
	"""docstring for Ploy"""
	def __init__(self, coeff):
		self.coeff = coeff
	
	def __call__(self, x):
		l = len(self.coeff)
		x_l = [x] * l
		x_p = np.array(x_l)
		poly_sum = self.coeff @ x_p
		return poly_sum

# p = Ploy([2,2,3,4])
# print(p(2))


## Exercise 2

from random import uniform
import numpy as np
# def sample(q):
# 	a =0.0
# 	U = uniform(0,1)
# 	for i in range(len(q)):
# 		if a < U <= a+q[i]:
# 			return i
# 			print(i)
# 		a = a+q[i]

# class DiscreteRV:
# 	"""docstring for DiscreteRV"""
# 	def __init__(self, q):
# 		self.q = q

# 	def draw(self,k):
# 		interval = np.cumsum(self.q)
# 		U = np.random.uniform(size =k)
# 		result = interval.searchsorted(U)
# 		print(result)
# 		return result


## Exercise 3
class ECDF:
	"""docstring for ECDF, empirical cumulative distr function"""
	def __init__(self, observations):
		self.observations = observations

	def __call__(self, x):
		obs = np.array(self.observations)
		prob = np.mean(obs <= x)
		print (prob)

	# def plot(self, ax, a=None, b=None):
		


		
samples = [uniform(0, 1) for i in range(100)]
# print(samples)
F = ECDF(samples)
F(0.7)

		