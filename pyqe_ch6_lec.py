class Consumer:
	"""docstring for Consumer"""
	def __init__(self, w):
		self.wealth = w
		print(self.wealth)
	def earn(self, y):
		self.wealth += y
		print(self.wealth)
	def spend(self, x):
		new_wealth = self.wealth -x
		if new_wealth > 0:
			self.wealth = new_wealth
			print(self.wealth)
		else:
			print ('Insufficient Fund')
wang = Consumer(1000)

import matplotlib.pyplot as plt

class Solow:
	"""docstring for Solow
		k_{t+1} = [(s z k^α_t) + (1 - δ)k_t] /(1 + n)
	"""
	def __init__(self, n =0.05, s =0.25, delta = 0.1,\
		alpha = 0.3, z = 2.0, k=1.0):
		self.n, self.s, self.delta,self.alpha,\
		 self.z, self.k = n, s, delta, alpha, z, k

	def h(self):
		n, s, delta, alpha, z = self.n, self.s, \
		self.delta,self.alpha, self.z

		return (s * z * self.k ** alpha +(1-delta)*self.k) / (1+n)

	def update(self):
		self.k =self.h()
	
	def steady_state(self):
		n, s, delta, alpha, z= self.n, self.s, \
		self.delta,self.alpha, self.z,
		
		return ((s*z)/(n+delta))**(1/(1-alpha))

	def generate_sequence(self, t):
		path =[]
		for i in range(t):
			path.append(self.k)
			self.update()
		return path

s1 = Solow()
s2 = Solow(k=8.0)

T = 90
fig, ax = plt.subplots(figsize=(9, 6))
ax.plot([s1.steady_state()]*T, 'k-', label='steady state')
for s in s1, s2:
	lb = f'capital series from initial state {s.k}' 
	ax.plot(s.generate_sequence(T), 'o-', lw=2, alpha=0.6, label=lb)
ax.set_xlabel('$k_{t+1}$', fontsize=14)
ax.set_ylabel('$k_t$', fontsize=14)
ax.legend()
plt.show()


