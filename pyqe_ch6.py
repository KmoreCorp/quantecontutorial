from random import uniform

class ECDF:
	"""docstring for ECDF, empirical cumulative distr function"""
	def __init__(self, observations):
		self.observations = observations

	def __call__(self, x):
		count = sum(s < x for s in self.observations)
		print (count/len(self.observations))

samples = [uniform(0, 1) for i in range(100)]
# print(samples)
F = ECDF(samples)
F(0.7)

F.observations = ([uniform(0, 1) for i in range(100000)])
F(0.7)


class Polynomial:
	"""docstring for Polynomial"""
	def __init__(self, coeff):
		self.coeff = coeff

	def __call__(self,x):
		s = sum(a*x**i for i,a in enumerate(self.coeff))
		return s

	def diff(self):
		new_coeff = [a*i for i, a in enumerate(self.coeff)]
		self.coeff = new_coeff
		return self.coeff
a = [2,5,8,7,6]
p = Polynomial(a)
print(p(1))
p.diff()
print(p(1))